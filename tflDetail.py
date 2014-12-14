import xmltodict, time

class TFLDetail(object):
	def __init__(self, xml, epoch=time.time()):
		self.xmld = xmltodict.parse(xml)
		self.station 	= self._loadStation()
		self.trains		= self._loadTrains(self.xmld)

	def _loadStation(self):
		return TFLDetailStation(self.xmld)

	def _loadTrains(self, xmld):
		ret = []
		for xmlPlat in xmld['ROOT']['S']['P']:
			if 'T' not in xmlPlat.keys(): 
				#no trains in platform, return None
				return None
			
			trains = xmlPlat['T']
			if type(trains) is not list:
				trains = [trains]
			for train in trains:
				ret.append( TFLDetailTrain(train) )
		return ret

	def __repr__(self):
		return "<tflDetail.TFLDetail: %s @ %s>" % (self.station.name, self.station.line_name)

class TFLDetailStation(object):
	def __init__(self, xmld):
		self.name 		= xmld['ROOT']['S']['@N'].replace(".", "")
		self.code 		= xmld['ROOT']['S']['@Code']
		self.line 		= xmld['ROOT']['Line']
		self.line_name	= xmld['ROOT']['LineName']
		self.platforms 	= self._loadPlatforms(xmld)

	def _loadPlatforms(self, xmld):
		ret = []
		for xmlPlat in xmld['ROOT']['S']['P']:
			ret.append( TFLDetailPlatform(xmlPlat) )
		return ret

	def __repr__(self):
		return "<tflDetail.TFLDetailStation: %s @ %s>" % (self.name, self.line_name)

class TFLDetailPlatform(object):
	def __init__(self, platformXMLd):
		self.name		= platformXMLd['@N']
		self.trackCode 	= platformXMLd['@TrackCode']
		self.trains 	= self._loadTrains(platformXMLd)

	def _loadTrains(self, platformXMLd):
		ret = []
		trains = platformXMLd['T']
		if type(trains) is not list:
			trains = [trains]
		for train in trains:
			ret.append( TFLDetailTrain(train) )
		return ret

	def __repr__(self):
		return "<tflDetail.TFLDetailPlatform: %s>" % self.name

class TFLDetailTrain(object):
	def __init__(self, trainXMLd):
		self.lcid		= trainXMLd['@LCID']
		self.trackCode	= trainXMLd['@TrackCode']

	def __repr__(self):
		return "<tflDetail.TFLDetailTrain: LeadingCarID:%s>" % self.lcid