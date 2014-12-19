import unittest
from tflAPI import TFLapi
import vcr

my_vcr = vcr.VCR(
	serializer = 'json',
	cassette_library_dir = 'tests/fixtures/cassettes',
	record_mode = 'once',
	match_on = ['uri', 'method'],
)

import logging

logging.basicConfig() # you need to initialize logging, otherwise you will not see anything from vcrpy
vcr_log = logging.getLogger("vcr")
vcr_log.setLevel(logging.ERROR)

class TestTFLapiByURL(unittest.TestCase):
	def setUp(self):
		self.api = TFLapi()

	def test_VerifyCorrectURLFetched(self):
		with my_vcr.use_cassette('Detail-OXC-B.json'):
			detail = self.api.getDetailed(station="OXC", line="B")
			self.assertEqual(detail.station, "OXC")
			self.assertEqual(detail.line, "B")

	def test_VerifyPlatformsQuantities(self):
		#camden town has 4 northern line platforms
		with my_vcr.use_cassette('Detail-CTN-N.json'):
			detail = self.api.getDetailed(station="CTN", line="N")
			self.assertEqual(detail.station, "CTN")
			self.assertIsInstance(detail.platforms, list)
			self.assertEqual( len(detail.platforms), 4)

		#oxford circus has 2 bakerloo platforms
		with my_vcr.use_cassette('Detail-OXC-B.json'):
			detail = self.api.getDetailed(station="OXC", line="B")
			self.assertEqual(detail.station, "OXC")
			self.assertIsInstance(detail.platforms, list)
			self.assertEqual( len(detail.platforms), 2)

	def test_VerifyPlatformsIdentified(self):
		with my_vcr.use_cassette('Detail-CTN-N.json'):
			detail = self.api.getDetailed(station="CTN", line="N")
			self.assertEqual(detail.platforms[0].name, "Northbound - Platform 1")
			self.assertEqual(detail.platforms[1].name, "Southbound - Platform 2")
			self.assertEqual(detail.platforms[2].name, "Northbound - Platform 3")
			self.assertEqual(detail.platforms[3].name, "Southbound - Platform 4")

	def test_VerifyTrainsOnPlatforms(self):
		#need testcase for no trains on platforms
		with my_vcr.use_cassette('Detail-OXC-B(TrainCode).json'):
			detail = self.api.getDetailed(station="OXC", line="B")
			self.assertIsInstance(detail.platforms[0].trains, list)

			self.assertEqual(detail.platforms[0].trains[0].leadingcar_id, "1088720")
			self.assertEqual(detail.platforms[0].trains[0].set_number, "207")
			self.assertEqual(detail.platforms[0].trains[0].trip_number, "13")
			self.assertEqual(detail.platforms[0].trains[0].arrival_seconds, "24")
			self.assertEqual(detail.platforms[0].trains[0].arrival_time, "0:30")
			self.assertEqual(detail.platforms[0].trains[0].current_location, "Between Regents Park and Oxford Circus")
			self.assertEqual(detail.platforms[0].trains[0].destination, "Elephant and Castle")
			self.assertEqual(detail.platforms[0].trains[0].destination_code, "154")
			self.assertEqual(detail.platforms[0].trains[0].platform_departure_time, "15:44:35")
			self.assertEqual(detail.platforms[0].trains[0].interval_between_previous_train, "24")
			self.assertEqual(detail.platforms[0].trains[0].departed_current_station, "0")
			self.assertEqual(detail.platforms[0].trains[0].direction, "0")
			self.assertEqual(detail.platforms[0].trains[0].track_code, "TB391B")