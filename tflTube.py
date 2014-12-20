import requests, logging
from tflAPI import TFLapi


class TFL(object):
	def __init__(self):
		logging.getLogger("requests").setLevel(logging.WARNING)
		self.api = TFLapi()
		self.map = TFLTubeMap(self.api)
	
class TFLTubeMap(object):
	def __init__(self, api):
		self.api = api
		from tflStationNames import stations, lineStations

		linesList = [TFLLine("C", "Central"), TFLLine("B", "Bakerloo"), TFLLine("D", "District"), TFLLine("H", "Hammersmith & Circle"), TFLLine("J", "Jubilee"), TFLLine("M", "Metropolitan"), TFLLine("N", "Nothern"), TFLLine("P", "Piccadilly"), TFLLine("W", "Waterloo & City"), TFLLine("V", "Victoria")]
		stationsList = [TFLStation(code, name) for code, name in stations.iteritems()]

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
		self._lines 		= TFLLineManager()
		self._stations	= TFLStationManager()

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
			return TFLStationLinePlatform(	self._stations[stationcode], 
											self._lines[linecode],
											self.api)

class TFLTrain(object):
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
		return "<tflTube.TFLTrain LCID(%s) on %s at %s>" % (self.leadingcar_id, self.line.name + " Line", self.current_location)

class TFLPlatform(object):
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
		return "<tflTube.TFLPlatform: %s %s >" % (self.line.name, self.name)

	def _getTrains(self):
		detailTrains = self._detailPlatform.trains
		self._loadTrainFromDetail(detailTrains, self.line)

	def _loadTrainFromDetail(self, detailTrains, line):
		for d in detailTrains:
			newT = TFLTrain()
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

class TFLStationLinePlatform(object):
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
			newP = TFLPlatform(self.api, p, self.line)
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


class TFLStation(object):
	def __init__(self, code, name):
		self.code 		= code
		self.name 		= name
		self._lines 	= TFLLineManager()

	def __repr__(self):
		return "<tflTube.TFLStation: %s>" % self.name

	def getLines(self):
		return self._lines

	def getAllTrains(self):
		ret = {}
		for l in self._lines:
			ret.update( trains = TFL().map.get(linecode=l, stationcode=self.code).getAllTrains() )
		return ret


class TFLStationManager(dict):
	def __init__(self):
		pass
	def addStation(self, station):
		if not self.has_key(station.code):
			self[station.code] = station

class TFLLine(object):
	def __init__(self, code, name):
		self.code 		= code
		self.name 		= name
		self._stations 	= TFLStationManager()

	def __repr__(self):
		return "<tflTube.TFLLine: %s>" % self.name

	def getStations(self):
		return self._stations

	def getAllTrains(self):
		ret = {}
		for stat in self._stations:
			tfl = TFL()
			ret.update( tfl.map.get(linecode=self.code, stationcode=stat).getAllTrains() )
		return ret

class TFLLineManager(dict):
	def __init__(self):
		pass			
	def addLine(self, line):
		if not self.has_key(line.code):
			self[line.code] = line

