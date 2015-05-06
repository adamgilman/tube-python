'''
Warning, this is an "private" class to the TFL object
You shouldn't reference this directly in your code as
there is minimal type checking and exception handling
'''
import requests, xmltodict
from collections import OrderedDict

class TFLapi(object):

	def __init__(self):
		self.detail_url = "http://cloud.tfl.gov.uk/TrackerNet/PredictionDetailed/%(line)s/%(station)s"

	def _getDetailedXML(self, station, line):
		url = self.detail_url % { 'station' : station, 'line' : line}
		rxml = requests.get(url).text.replace(u"\xef\xbb\xbf", "") #strange unicode error
		return rxml

	def getDetailed(self, station=None, line=None):
		if (station is None) or (line is None):
			return None

		return APIDetail(xml=self._getDetailedXML(station, line) )


class APIDetail(object):
	def __init__(self, xml=None):
		if xml is None:
			Exception("Need XML")
		self.xml = xml
		self.xmlDict = xmltodict.parse(self.xml)

		self.station = None
		self.line = None
		self._processHeader()

		self.platforms = []
		self._processPlatforms()


	def _processHeader(self):
		self.line = self.xmlDict['ROOT']['Line']
		self.station = self.xmlDict['ROOT']['S']['@Code']

	def _processPlatforms(self):
		platforms = self.xmlDict['ROOT']['S']['P']
		for plat in platforms:
			self.platforms.append( DetailPlatform(plat) )


class DetailPlatform(object):
	def __init__(self, xmlDict):
		self.trains = []
		self.name = None
		self.platform_number = None
		self.track_code = None
		self.next_train = None
		
		self.xmlDict = xmlDict
		if type(xmlDict) is OrderedDict:
			self.name = xmlDict['@N']
			self.platform_number = xmlDict['@Num']
			self.track_code = xmlDict['@TrackCode']
			self.next_train = xmlDict['@NextTrain']

			self._processTrains()


	def _processTrains(self):
		if self.xmlDict.has_key('T'):
			trains = self.xmlDict['T']
			for t in trains:
				try:
					self.trains.append( DetailTrain(t) )
				except:
					#TODO: May be dropping a train on the floor here
					pass


class DetailTrain(object):
	def __init__(self, xmlDict):
		if (type(xmlDict) is not OrderedDict):
			raise Exception("xmlDict does not contain a train")
		self.xmlDict = xmlDict
		#'true' if True else 'false'
		self.leadingcar_id = xmlDict["@LCID"]
		self.set_number = xmlDict['@SetNo']
		self.trip_number = xmlDict['@TripNo']
		self.arrival_seconds = xmlDict['@SecondsTo']
		self.arrival_time = xmlDict['@TimeTo']
		self.current_location = xmlDict['@Location']
		self.destination = xmlDict['@Destination']
		self.destination_code = xmlDict['@DestCode']
		self.platform_departure_time = xmlDict['@DepartTime']
		self.interval_between_previous_train = xmlDict['@DepartInterval']
		self.departed_current_station = xmlDict['@Departed']
		self.direction = xmlDict['@Direction']
		self.track_code = xmlDict['@TrackCode']
