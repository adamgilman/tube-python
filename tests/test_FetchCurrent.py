import unittest
from tflTube import TFL
from tflTube import TFLLine, TFLStation, TFLStationLinePlatform, TFLPlatform

import vcr

my_vcr = vcr.VCR(
	serializer = 'json',
	cassette_library_dir = 'tests/fixtures/cassettes',
	record_mode = 'once',
)

import logging

logging.basicConfig() # you need to initialize logging, otherwise you will not see anything from vcrpy
vcr_log = logging.getLogger("vcr")
vcr_log.setLevel(logging.DEBUG)

class TestTFLPlatforms(unittest.TestCase):
	def setUp(self):
		self.tfl = TFL()
		self.current = self.tfl.map

	def test_GetPlatforms(self):
		with my_vcr.use_cassette('Detail-OXC-B.json'):
			platforms = self.tfl.map.get(linecode="B", stationcode="OXC").platforms
			self.assertIsInstance( platforms, dict)

			first_platform = platforms[platforms.keys()[0]]
			self.assertIsInstance( first_platform, TFLPlatform)
			self.assertEqual( first_platform.name, "Northbound - Platform 4")

class TestTFLTubeMap(unittest.TestCase):
	def setUp(self):
		self.tfl = TFL()
		self.current = self.tfl.map

	def test_GetStation(self):
		with my_vcr.use_cassette('Detail-OXC-B.json'):
			self.assertIsInstance(self.tfl.map.get(stationcode="OXC"), TFLStation)
			self.assertIsNone(self.tfl.map.get(stationcode="XXX"))
			self.assertIsNone(self.tfl.map.get())

	def test_GetLine(self):
		with my_vcr.use_cassette('Detail-OXC-B.json'):
			self.assertIsInstance(self.tfl.map.get(linecode="B"), TFLLine)
			self.assertIsNone(self.tfl.map.get(linecode="X"))
			self.assertIsNone(self.tfl.map.get())

	def test_GetStationLine(self):
		with my_vcr.use_cassette('Detail-OXC-B.json'):
			self.assertIsInstance(self.tfl.map.get(linecode="B", stationcode="OXC"), TFLStationLinePlatform)
		with my_vcr.use_cassette('Detail-OXC-B.json'):
			self.assertIsInstance(self.tfl.map.get(linecode="B", stationcode="OXC").station, TFLStation)
		with my_vcr.use_cassette('Detail-OXC-B.json'):
			self.assertEqual(self.tfl.map.get(linecode="B", stationcode="OXC").station.code, "OXC")
		with my_vcr.use_cassette('Detail-OXC-B.json'):
			self.assertIsInstance(self.tfl.map.get(linecode="B", stationcode="OXC").line, TFLLine)
		with my_vcr.use_cassette('Detail-OXC-B.json'):
			self.assertEqual(self.tfl.map.get(linecode="B", stationcode="OXC").line.code, "B")

	def test_FailGetStationLine(self):
		#district line does not go through OXC
		self.assertIsNone(self.tfl.map.get(linecode="D", stationcode="OXC"))
