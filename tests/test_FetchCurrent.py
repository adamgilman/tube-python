import unittest
from tflTube import TFL
from tflTube import TFLLine, TFLStation

'''
	def test_InvalidStationOnLine(self):
		self.assertIsNone(self.status.getStatus("D", "OXC"))
		self.assertIsNotNone(self.status.getStatus("V", "OXC"))
		self.assertIsNotNone(self.status.getStatus("B", "OXC"))
		self.assertIsNotNone(self.status.getStatus("C", "OXC"))

	def test_NumberPlatformsAtStation(self):
		v_bhr = self.status.getStatus("V", "BHR")
		self.assertEqual(len(v_bhr.platforms), 2)

	def test_NextTrainsOnPlatform(self):
		print self.status.getStatus("V", "OXC")
		self.assertTrue(False)
'''

class TestTFLFetchCurrent(unittest.TestCase):
	def setUp(self):
		self.tfl = TFL()

	def test_GetPlatformInvalidStationOnLine(self):
		#self.assertIsNone( self.tfl.getPlatforms(self.tfl.map.stations['OXC'], self.tfl.map.lines['D']) )
		#self.assertIsNotNone( self.tfl.getPlatforms(self.tfl.map.stations['OXC'], self.tfl.map.lines['C']) )
		pass

	def test_GetPlatformsOnStationLine(self):
		#platforms = self.tfl.getPlatforms(self.tfl.map.stations['OXC'], self.tfl.map.lines['B'])
		#self.assertIsInstance(platforms, dict)
		#self.assertIsInstance(platforms.iteritems().next(), TFLPlatform)
		pass
		#self.assertIsInstance(platforms[0].name, unicode)
		#self.assertTrue( len(platforms[0].name) is not 0 )
	
#	def test_GetNextTrainsOnPlatform(self):
#		platforms = self.tfl.getPlatforms(self.tfl.map.stations['OXC'], self.tfl.map.lines['B'])
#		self.assertIsInstance( platforms[0].trains, list)

		#self.assertIsInstance( platforms[0].trains[0], TFLTrain)



class TestTFLTubeMap(unittest.TestCase):
	def setUp(self):
		self.tfl = TFL()
		self.current = self.tfl.map

	def test_GetStation(self):
		self.assertIsInstance(self.tfl.map.get(stationcode="OXC"), TFLStation)
		self.assertIsNone(self.tfl.map.get(stationcode="XXX"))
		self.assertIsNone(self.tfl.map.get())

	def test_GetLine(self):
		self.assertIsInstance(self.tfl.map.get(linecode="B"), TFLLine)
		self.assertIsNone(self.tfl.map.get(linecode="X"))
		self.assertIsNone(self.tfl.map.get())

	def test_GetStationLine(self):
		self.assertIsInstance(self.tfl.map.get(linecode="B", stationcode="OXC"), dict)
		self.assertIsInstance(self.tfl.map.get(linecode="B", stationcode="OXC")['station'], TFLStation)
		self.assertIsInstance(self.tfl.map.get(linecode="B", stationcode="OXC")['line'], TFLLine)

	def test_FailGetStationLine(self):
		#district line does not go through OXC
		self.assertIsNone(self.tfl.map.get(linecode="D", stationcode="OXC"))


	#self.assertEqual(len(self.current.stations), 263)
