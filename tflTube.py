import requests, logging
from tflAPI import TFLapi


class TFL(object):
	def __init__(self):
		logging.getLogger("requests").setLevel(logging.WARNING)
		self.map = TFLTubeMap()
		self.api = TFLapi()

'''
	def getPlatforms(self, station, line):
		if (type(station) is not TFLStation) and (type(line) is not TFLLine):
			raise Exception("Must pass TFLStation and TFLLine objects, utilize TFL.map")
		#check station is on line (e.g. OXC doesn't have District line)
		if line.code not in station.lines.keys():
			return None

		detail = self.api.getDetailed(station=station.code, line=line.code)
		for plat in detail.platforms:
			pass

		return {}
'''

class TFLPlatform(object):
	
	def __init__(self, detailPlatform=None):
		if detailXML is not None:
			pass

	def __repr__(self):
		return "<tflTube.TFLPlatform: %s>" % self.name

class TFLStation(object):
	def __init__(self, code, name):
		self.code 		= code
		self.name 		= name
		self.lines 		= TFLLineManager()
		self.platforms 	= TFLPlatformManager(self)

	def __repr__(self):
		return "<tflTube.TFLStation: %s>" % self.name

class TFLPlatformManager(dict):
	def __init__(self, station):
		self.station = station
		self.lines = {}
		for line in self.station.lines:
			print line
			self.lines[line] = []



class TFLTubeMap(object):
	def __init__(self):
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
				stations[scode].lines.addLine(line)
				#add line to station		
				lines[lcode].stations.addStation(station)

		#stations are mapped to lines, create root managers
		self.lines 		= TFLLineManager()
		self.stations	= TFLStationManager()

		self.lines.update(lines)
		self.stations.update(stations)

class TFLStationManager(dict):
	def __init__(self):
		pass
	def addStation(self, station):
		if not self.has_key(station.code):
			self[station.code] = station
	def getStation(self, stationcode):
		if self.has_key(stationcode):
			return self[stationcode]
		else:
			return None

class TFLLine(object):
	def __init__(self, code, name):
		self.code 		= code
		self.name 		= name
		self.stations 	= TFLStationManager()

	def __repr__(self):
		return "<tflTube.TFLLine: %s>" % self.name

class TFLLineManager(dict):
	def __init__(self):
		pass			
	def addLine(self, line):
		if not self.has_key(line.code):
			self[line.code] = line
	def getLine(self, linecode):
		if self.has_key(linecode):
			return self[linecode]
		else:
			return None

