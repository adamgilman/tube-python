import requests, logging
from tflAPI import TFLapi


class Tube(object):
	'''Root Tube object. Explore the underground with the .map object'''
	def __init__(self):
		logging.getLogger("requests").setLevel(logging.WARNING)
		self._api = TFLapi()
		self.map = TubeMap(self._api)

	@property
	def lines(self):
		return self.map.allLines()
	
	@property
	def stations(self):
		return self.map.allStations()

	def getAllTrainsForStation(self, station):
		if type(station) is TubeStation:
			station = station.code
		trains = self.map.get(stationcode=station).getAllTrains().values()
		return trains

	def getAllTrainsForLine(self, line):
		if type(line) is TubeLine:
			line = line.code
		trains = self.map.get(linecode=line).getAllTrains().values()
		return trains

class TubeMap(object):
	'''Object representation of the underground
			access single stations or line with .get
				.get(stationcode='OXC')
				.get(linecode='V')
			get all lines and stations with .all*
				.allLines()
				.allStations()

			get associated lines with stations via property
				.get(stationcode='OXC').getLines()

			get associated stations with lines via property
				.get(linecode='V').getStations()
	'''
	def __init__(self, api):
		from tflStationNames import stations, lineStations
		self._api = api
		linesList = [TubeLine("C", "Central"), TubeLine("B", "Bakerloo"), TubeLine("D", "District"), TubeLine("H", "Hammersmith & Circle"), TubeLine("J", "Jubilee"), TubeLine("M", "Metropolitan"), TubeLine("N", "Nothern"), TubeLine("P", "Piccadilly"), TubeLine("W", "Waterloo & City"), TubeLine("V", "Victoria")]
		stationsList = [TubeStation(code, name) for code, name in stations.iteritems()]

		lines = {} #TODO: rewrite by comprehension
		for line in linesList:
			lines[line.code] = line

		stations = {} #TODO: rewrite by comprehension
		for station in stationsList:
			stations[station.code] = station

		for lcode in lineStations.keys():
			for scode in lineStations[lcode]:
				line = lines[lcode]
				station = stations[scode]
				#add station to line
				stations[scode]._lines.addLine(line)
				#add line to station
				lines[lcode]._stations.addStation(station)

		#stations are mapped to lines, create root managers
		self._lines 	= TubeLineManager()
		self._stations	= TubeStationManager()

		self._lines.update(lines)
		self._stations.update(stations)

	def _validstationcode(self, stationcode):
		if stationcode is not None:
			return stationcode in self._stations.keys()
		else:
			return None

	def _validlinecode(self, linecode):
		if linecode is not None:
			return linecode in self._lines.keys()
		else:
			return None

	def allStations(self):
		return self._stations

	def allLines(self):
		return self._lines

	def getStation(self, stationcode=None): return self.get(stationcode=stationcode)
	def getLine(self, linecode=None): return self.get(linecode=linecode)

	def get(self, stationcode=None, linecode=None):
		#valid station but, not line
		if (self._validstationcode(stationcode)) and not (self._validlinecode(linecode)):
			return self._stations[stationcode]
		#valid line but, not station
		if not (self._validstationcode(stationcode)) and (self._validlinecode(linecode)):
			return self._lines[linecode]
		#valid line and station
		if (self._validstationcode(stationcode)) and (self._validlinecode(linecode)):
			#check if station is on line
			if linecode not in self._stations[stationcode]._lines.keys():
				return None
			return TubeStationLinePlatform(	self._stations[stationcode],
											self._lines[linecode],
											self._api)
		raise KeyError("stationcode or linecode does not exist, refer to allLines or allStations for valid codes")

class TubeTrain(object):
	def __init__(self):
		self.line = None
		self.leadingcar_id = None
		self.set_number = None
		self.trip_number = None
		self.arrival_seconds = None
		self.arrival_time = None
		self.current_location = None
		self.destination = None
		self.destination_code = None
		self.platform_departure_time = None
		self.interval_between_previous_train = None
		self.departed_current_station = None
		self.direction = None
		self.track_code = None

	def __repr__(self):
		return "<Tube.Train LCID(%s) on %s at %s>" % (self.leadingcar_id, self.line.name + " Line", self.current_location)

class TubePlatform(object):
	def __init__(self, api, detailPlatform, line):
		self.api = api
		self._detailPlatform = detailPlatform
		self.name = None
		self.platform_number = None
		self.track_code = None
		self.next_train = None
		self.trains	= {}
		self.line = line

		self._getTrains()

	def __repr__(self):
		return "<Tube.Platform: %s %s >" % (self.line.name, self.name)

	def _getTrains(self):
		detailTrains = self._detailPlatform.trains
		self._loadTrainFromDetail(detailTrains, self.line)

	def _loadTrainFromDetail(self, detailTrains, line):
		for d in detailTrains:
			newT = TubeTrain()
			newT.line = line
			newT.leadingcar_id = d.leadingcar_id
			newT.set_number = d.set_number
			newT.trip_number = d.trip_number
			newT.arrival_seconds = d.arrival_seconds
			newT.arrival_time = d.arrival_time
			newT.current_location = d.current_location
			newT.destination = d.destination
			newT.destination_code = d.destination_code
			newT.platform_departure_time = d.platform_departure_time
			newT.interval_between_previous_train = d.interval_between_previous_train
			newT.departed_current_station = d.departed_current_station
			newT.direction = d.direction
			newT.track_code = d.track_code
			self.trains[newT.leadingcar_id] = newT

class TubeStationLinePlatform(object):
	def __init__(self, station, line, api):
		self.api 		= api
		self.station 	= station
		self.line 		= line
		self.platforms 	= {}

		self._getPlatforms()

	def _getPlatforms(self):
		details = self.api.getDetailed(self.station.code, self.line.code)
		self._loadPlatformsFromDetail(details.platforms)

	def _loadPlatformsFromDetail(self, detailPlatforms):
		for p in detailPlatforms:
			newP = TubePlatform(self.api, p, self.line)
			newP.name = p.name
			newP.platform_number = p.platform_number
			newP.track_code = p.platform_number
			newP.next_train = p.track_code
			self.platforms[newP.name] = newP

	def getAllTrains(self):
		ret = {}
		for plat in self.platforms.keys():
			ret.update(self.platforms[plat].trains)
		return ret


class TubeStation(object):
	def __init__(self, code, name):
		self.code 		= code
		self.name 		= name
		self._lines 	= TubeLineManager()

	def __repr__(self):
		return "<Tube.Station: %s>" % self.name

	def getLines(self):
		return self._lines

	def getAllTrains(self):
		ret = {}
		for l in self._lines:
			ret.update(Tube().map.get(linecode=l, stationcode=self.code).getAllTrains() )
		return ret


class TubeStationManager(dict):
	def __init__(self):
		pass
	def addStation(self, station):
		if not self.has_key(station.code):
			self[station.code] = station

class TubeLine(object):
	def __init__(self, code, name):
		self.code 		= code
		self.name 		= name
		self._stations 	= TubeStationManager()

	def __repr__(self):
		return "<Tube.Line: %s>" % self.name

	def getStations(self):
		return self._stations

	def getAllTrains(self):
		ret = {}
		for stat in self._stations:
			tfl = Tube()
			ret.update( tfl.map.get(linecode=self.code, stationcode=stat).getAllTrains() )
		return ret

class TubeLineManager(dict):
	def __init__(self):
		pass
	def addLine(self, line):
		if not self.has_key(line.code):
			self[line.code] = line
