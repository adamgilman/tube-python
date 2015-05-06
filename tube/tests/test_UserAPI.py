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

class TestUserAPIAccess(unittest.TestCase):
    def setUp(self):
        self.tube = Tube()

    def test_getAllTrainsForStation(self):
        with my_vcr.use_cassette('User-All-Station-KXX.json'):
            trains = self.tube.getAllTrainsForStation("KXX")
            self.assertIsInstance( trains, list )
            self.assertIsInstance( trains[0], TubeTrain )
            self.assertEqual( len(trains), 110 )
        with my_vcr.use_cassette('User-All-Station-KXX.json'):
            kxx = self.tube.map.get(stationcode="KXX")
            trains = self.tube.getAllTrainsForStation(kxx)
            self.assertIsInstance( trains, list )
            self.assertIsInstance( trains[0], TubeTrain )
            self.assertEqual( len(trains), 110 )

    def test_getAllTrainsForLine(self):
        with my_vcr.use_cassette('User-All-Line-North.json'):
            trains = self.tube.getAllTrainsForLine("N")
            self.assertIsInstance( trains, list )
            self.assertIsInstance( trains[0], TubeTrain )
            self.assertEqual( len(trains), 152 )
        with my_vcr.use_cassette('User-All-Line-North.json'):
            northern = self.tube.map.get(linecode="N")
            trains = self.tube.getAllTrainsForLine(northern)
            self.assertIsInstance( trains, list )
            self.assertIsInstance( trains[0], TubeTrain )
            self.assertEqual( len(trains), 152 )
