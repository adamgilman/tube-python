import unittest
from tflTube import TFL
from tflTube import TFLLine, TFLStation, TFLTrain, TFLPlatform

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
		self.assertIsNone( self.tfl.getPlatforms(self.tfl.map.stations['OXC'], self.tfl.map.lines['D']) )
		self.assertIsNotNone( self.tfl.getPlatforms(self.tfl.map.stations['OXC'], self.tfl.map.lines['C']) )


	def test_GetPlatformsOnStationLine(self):
		platforms = self.tfl.getPlatforms(self.tfl.map.stations['OXC'], self.tfl.map.lines['B'])
		self.assertIsInstance(platforms, list)

		self.assertIsInstance(platforms[0], TFLPlatform)

		self.assertIsInstance(platforms[0].name, unicode)
		self.assertTrue( len(platforms[0].name) is not 0 )
	
#	def test_GetNextTrainsOnPlatform(self):
#		platforms = self.tfl.getPlatforms(self.tfl.map.stations['OXC'], self.tfl.map.lines['B'])
#		self.assertIsInstance( platforms[0].trains, list)

		#self.assertIsInstance( platforms[0].trains[0], TFLTrain)



class TestTFLTubeMap(unittest.TestCase):
	def setUp(self):
		self.tfl = TFL()
		self.current = self.tfl.map
		
	def test_HasTubeLines(self):
		self.assertIsInstance(self.current.lines.getLine("V"), TFLLine)
		self.assertNotIsInstance(self.current.lines.getLine("X"), TFLLine)
		self.assertIsNone(self.current.lines.getLine("X"))

		self.assertEqual(self.current.lines.getLine("V").name, "Victoria")
		self.assertEqual(self.current.lines.getLine("V").code, "V")
		self.assertEqual(self.current.lines["V"].name, "Victoria")

		self.assertEqual(len(self.current.lines), 10)

	def test_HasTubeStations(self):
		self.assertIsInstance(self.current.stations.getStation("OXC"), TFLStation)
		self.assertNotIsInstance(self.current.stations.getStation("X"), TFLStation)
		self.assertIsNone(self.current.stations.getStation("X"))

		self.assertEqual(self.current.stations.getStation("OXC").name, "Oxford Circus")
		self.assertEqual(self.current.stations.getStation("KXX").code, "KXX")
		self.assertEqual(self.current.stations['KXX'].name, "King's Cross St Pancras")

		self.assertEqual(len(self.current.stations), 263)


	def test_HasStationOnLine(self):
		self.assertTrue(set(['OLD', 'KXX']).issubset(self.current.lines['N'].stations.keys()) )
		self.assertTrue(set(['OXC', 'HBY', 'KXX']).issubset(self.current.lines['V'].stations.keys()) )

	def test_HasLineOnStation(self):
		self.assertTrue(set(['V', 'C']).issubset(self.current.stations['OXC'].lines.keys()) )
		self.assertTrue(set(['V', 'N']).issubset(self.current.stations['KXX'].lines.keys()) )

