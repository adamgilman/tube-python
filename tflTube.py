import requests, logging
from tflAPI import TFLapi


class TFL(object):
	def __init__(self):
		logging.getLogger("requests").setLevel(logging.WARNING)
		self.map = TFLTubeMap()
	
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
			return {'station' : self._stations[stationcode], 'line' : self._lines[linecode]}

class TFLStation(object):
	def __init__(self, code, name):
		self.code 		= code
		self.name 		= name
		self._lines 	= TFLLineManager()

	def __repr__(self):
		return "<tflTube.TFLStation: %s>" % self.name

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

class TFLLineManager(dict):
	def __init__(self):
		pass			
	def addLine(self, line):
		if not self.has_key(line.code):
			self[line.code] = line

