import unittest
from tube.tubeAPI import Tube
from tube.tubeAPI import TubeLine, TubeStation, TubeStationLinePlatform
from tube.tubeAPI import TubePlatform, TubeTrain

import vcr

my_vcr = vcr.VCR(
	serializer = 'json',
	cassette_library_dir = 'tube/tests/fixtures/cassettes',
	record_mode = 'once',
)

import logging

logging.basicConfig() # you need to initialize logging, otherwise you will not see anything from vcrpy
vcr_log = logging.getLogger("vcr")
vcr_log.setLevel(logging.DEBUG)

class TestFriendlyTrainsAccess(unittest.TestCase):
	def setUp(self):
		self.tube = Tube()
	
	def test_GetAllTrainsLineStation(self):
		with my_vcr.use_cassette('Detail-OXC-B.json'):
			trains = self.tube.map.get(linecode="B", stationcode="OXC").getAllTrains()
			self.assertIsInstance( trains, dict )
			self.assertIsInstance( trains[trains.keys()[0]], TubeTrain)
			self.assertEqual( len(trains), 14)

		
	def test_GetAllTrainsLine(self):
		with my_vcr.use_cassette('Detail-Friendly-GetAll.json'):
			trains = self.tube.map.get(linecode="V").getAllTrains()
			self.assertIsInstance( trains, dict )
		
	def test_GetAllTrainsStation(self):
		with my_vcr.use_cassette('Detail-Friendly-GetAll-Station.json'):
			trains = self.tube.map.get(stationcode="OXC").getAllTrains()


class TestTubePlatforms(unittest.TestCase):
	def setUp(self):
		self.tube = Tube()
		self.current = self.tube.map

	def test_GetPlatformsAtStationLine(self):
		with my_vcr.use_cassette('Detail-OXC-B.json'):
			platforms = self.tube.map.get(linecode="B", stationcode="OXC").platforms
			self.assertIsInstance( platforms, dict)

			first_platform = platforms[platforms.keys()[0]]
			self.assertIsInstance( first_platform, TubePlatform)
			self.assertEqual( first_platform.name, "Northbound - Platform 4")

class TestTubeTrains(unittest.TestCase):
	def setUp(self):
		self.tube = Tube()
	def test_GetTrainsOnPlatform(self):
		with my_vcr.use_cassette('Detail-OXC-B.json'):
			platforms = self.tube.map.get(linecode="B", stationcode="OXC").platforms
			first_platform = platforms[platforms.keys()[0]]
			self.assertIsInstance( first_platform.trains, dict)

			first_train = first_platform.trains[first_platform.trains.keys()[0]]
			self.assertIsInstance( first_train, TubeTrain )

			second_train = first_platform.trains[first_platform.trains.keys()[1]]
			self.assertEqual( first_train.leadingcar_id, "1030276" )
			self.assertEqual( second_train.destination, "Queen's Park")


class TestTubeMap(unittest.TestCase):
	def setUp(self):
		self.tube = Tube()
		self.current = self.tube.map

	def test_GetStation(self):
		with my_vcr.use_cassette('Detail-OXC-B.json'):
			self.assertIsInstance(self.tube.map.get(stationcode="OXC"), TubeStation)
			self.assertRaises(self.tube.map.get, stationcode="XXX")
			self.assertRaises(self.tube.map.get)

	def test_GetLine(self):
		with my_vcr.use_cassette('Detail-OXC-B.json'):
			self.assertIsInstance(self.tube.map.get(linecode="B"), TubeLine)
			self.assertRaises(self.tube.map.get, linecode="XXX")
			self.assertRaises(self.tube.map.get)

	def test_GetStationLine(self):
		with my_vcr.use_cassette('Detail-OXC-B.json'):
			self.assertIsInstance(self.tube.map.get(linecode="B", stationcode="OXC"), TubeStationLinePlatform)
		with my_vcr.use_cassette('Detail-OXC-B.json'):
			self.assertIsInstance(self.tube.map.get(linecode="B", stationcode="OXC").station, TubeStation)
		with my_vcr.use_cassette('Detail-OXC-B.json'):
			self.assertEqual(self.tube.map.get(linecode="B", stationcode="OXC").station.code, "OXC")
		with my_vcr.use_cassette('Detail-OXC-B.json'):
			self.assertIsInstance(self.tube.map.get(linecode="B", stationcode="OXC").line, TubeLine)
		with my_vcr.use_cassette('Detail-OXC-B.json'):
			self.assertEqual(self.tube.map.get(linecode="B", stationcode="OXC").line.code, "B")

	def test_FailGetStationLine(self):
		#district line does not go through OXC
		self.assertIsNone(self.tube.map.get(linecode="D", stationcode="OXC"))
