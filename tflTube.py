from tflDetail import TFLDetail
import requests, logging


class TFL(object):
	def __init__(self):
		logging.getLogger("requests").setLevel(logging.WARNING)
		self.map = TFLTubeMap()

	def getPlatforms(self, station, line):
		if (type(station) is not TFLStation) and (type(line) is not TFLLine):
			raise Exception("Must pass TFLStation and TFLLine objects, utilize TFL.map")
		
		#check station is on line (e.g. OXC doesn't have District line)
		if line.code not in station.lines.keys():
			return None


		url = "http://cloud.tfl.gov.uk/TrackerNet/PredictionDetailed/%s/%s" % (line.code, station.code)
		xml = requests.get(url).text.replace(u"\xef\xbb\xbf", "") #strange unicode error
		detail = TFLDetail(xml)
		
		platManager = TFLPlatformManager()
		for plat in detail.station.platforms:
			platManager.append( TFLPlatform(plat) )

		return platManager

		

class TFLTubeMap(object):
	def __init__(self):
		from tflStationNames import stations

		linesList = [TFLLine("C", "Central"), TFLLine("B", "Bakerloo"), TFLLine("D", "District"), TFLLine("H", "Hammersmith & Circle"), TFLLine("J", "Jubilee"), TFLLine("M", "Metropolitan"), TFLLine("N", "Nothern"), TFLLine("P", "Piccadilly"), TFLLine("W", "Waterloo & City"), TFLLine("V", "Victoria")]
		stationsList = [TFLStation(code, name) for code, name in stations.iteritems()]

		lines = {} #TODO: rewrite by comprehension
		for line in linesList:
			lines[line.code] = line

		stations = {} #TODO: rewrite by comprehension
		for station in stationsList:
			stations[station.code] = station

		#map stations to lines
		lineStations = {}
		lineStations['B'] = ['BST', 'CHX', 'ERB', 'ELE', 'EMB', 'HSD', 'HAW', 'KGN', 'KNT', 'KPK', 'LAM', 'MDV', 'MYB', 'NWM', 'OXC', 'PAD', 'QPK', 'RPK', 'SKT', 'SPK', 'WAR', 'WLO', 'WEM', 'WJN']
		lineStations['C'] = ['BNK', 'BDE', 'BNG', 'BDS', 'BHL', 'CYL', 'CHG', 'DEB', 'EBY', 'EAC', 'EPP', 'FLP', 'GHL', 'GRH', 'GFD', 'HAI', 'HLN', 'HOL', 'HPK', 'LAN', 'LEY', 'LYS', 'LST', 'LTN', 'MAR', 'MLE', 'NEP', 'NAC', 'NHT', 'NHG', 'OXC', 'PER', 'QWY', 'RED', 'ROD', 'RUG', 'SBC', 'SNB', 'SRP', 'SWF', 'STP', 'SFD', 'THB', 'TCR', 'WAN', 'WAC', 'WRP', 'WCT', 'WFD']
		lineStations['D'] = ['ACT', 'ALE', 'BKG', 'BCT', 'BEC', 'BLF', 'BWR', 'BBB', 'CST', 'CHP', 'DGE', 'DGH', 'EBY', 'ECM', 'ECT', 'EHM', 'EPY', 'ERD', 'EPK', 'EMB', 'FBY', 'GRD', 'GUN', 'HMD', 'HST', 'HCH', 'KEW', 'MAN', 'MLE', 'MON', 'OLY', 'PAD', 'PGR', 'PLW', 'PUT', 'RCP', 'RMD', 'SSQ', 'SKN', 'SFS', 'SJP', 'STB', 'STG', 'TEM', 'THL', 'TGR', 'UPM', 'UPB', 'UPY', 'UPK', 'VIC', 'WBT', 'WHM', 'WKN', 'WMS', 'WCL', 'WDN', 'WMP']
		lineStations['H'] = ['ALD', 'ALE', 'BST', 'BAR', 'BAY', 'BKG', 'BLF', 'BWR', 'BBB', 'CST', 'EHM', 'ERD', 'EMB', 'ESQ', 'FAR', 'GRD', 'GPS', 'HMS', 'HST', 'KXX', 'LBG', 'LST', 'MAN', 'MLE', 'MON', 'MGT', 'NHG', 'PAD', 'PAD', 'PAD', 'PLW', 'ROA', 'SSQ', 'SKN', 'SJP', 'STG', 'TEM', 'THL', 'UPK', 'VIC', 'WBP', 'WHM', 'WMS', 'WCL']
		lineStations['J'] = ['BST', 'BER', 'BDS', 'CWR', 'CWF', 'CNT', 'CPK', 'CHX', 'DHL', 'FRD', 'GPK', 'KIL', 'KBY', 'LON', 'NEA', 'NGW', 'QBY', 'SWK', 'SJW', 'STA', 'SFD', 'SWC', 'WLO', 'WPK', 'WHM', 'WHD', 'WMS', 'WLG']
		lineStations['M'] = ['ALD', 'AME', 'BST', 'BAR', 'BKG', 'CLF', 'CWD', 'CLW', 'CRX', 'ETE', 'ESQ', 'FAR', 'FRD', 'GPS', 'HOH', 'HDN', 'ICK', 'KXX', 'LST', 'MPK', 'MGT', 'NHR', 'NWP', 'NWD', 'NWH', 'PIN', 'RLN', 'RKY', 'RUI', 'RUM', 'UXB', 'WAT', 'WPK', 'WHR', 'WCL', 'WSP']
		lineStations['N'] = ['ANG', 'ARC', 'BAL', 'BNK', 'BPK', 'BOR', 'BTX', 'BUR', 'CTN', 'CHF', 'CHX', 'CPC', 'CPN', 'CPS', 'COL', 'CLW', 'EFY', 'EDG', 'ELE', 'EMB', 'EUS', 'FYC', 'GGR', 'GST', 'HMP', 'HND', 'HBT', 'HIG', 'KEN', 'KTN', 'KXX', 'LSQ', 'LON', 'MHE', 'MGT', 'MOR', 'MCR', 'OLD', 'OVL', 'SWM', 'STK', 'TBE', 'TBY', 'TCR', 'TOT', 'TPK', 'WST', 'WLO', 'WFY', 'WSP']
		lineStations['P'] = ['ACT', 'ALP', 'AGR', 'ARL', 'BCT', 'BOS', 'BGR', 'CRD', 'CFS', 'COV', 'ECM', 'ECT', 'ETE', 'FPK', 'GRD', 'GPK', 'HMD', 'HTX', 'HTF', 'HRV', 'HRC', 'HDN', 'HOL', 'HRD', 'HNC', 'HNE', 'HNW', 'HPC', 'ICK', 'KXX', 'KNB', 'LSQ', 'MNR', 'NEL', 'NFD', 'OAK', 'OST', 'PRY', 'PIC', 'RLN', 'RUI', 'RUM', 'RSQ', 'SEL', 'SHR', 'SKN', 'SGT', 'SHL', 'STN', 'TGR', 'TPL', 'UXB', 'WGN']
		lineStations['V'] = ['BHR', 'BRX', 'EUS', 'FPK', 'GPK', 'HBY', 'KXX', 'OXC', 'PIM', 'SVS', 'STK', 'TTH', 'VUX', 'VIC', 'WAL', 'WST']
		lineStations['W'] = ['BNK', 'WLO']

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

class TFLPlatformManager(list):
	def __init__(self):
		pass

class TFLPlatform(object):
	def __init__(self, detailPlat):
		self.name = detailPlat.name
		self.trains = self.getTrains(detailPlat)

	def getTrains(self, detailPlat):
		ret = []
		for detTrain in detailPlat.trains:
			ret.append( TFL )
		return []

class TFLTrain(object):
	def __init__(self, detailTrain=None):
		if detailTrain is not None:
			self._createFromDetailXMLTrain(detailTrain)

	def _createFromDetailXMLTrain(self, detailTrain):
		pass

class TFLStation(object):
	def __init__(self, code, name):
		self.code 		= code
		self.name 		= name
		self.lines 		= TFLLineManager()

	def __repr__(self):
		return "<tflTube.TFLStation: %s>" % self.name

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

