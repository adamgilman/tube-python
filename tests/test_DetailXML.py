import unittest
from tflDetail import TFLDetail

class TestDetailInformation(unittest.TestCase):
	def setUp(self): 
		path = "./tests/fixtures/"
		fn = "1418383518.874074_Detail_V_Victoria_BHR.xml"
		xml = open(path+fn).read()
		epoch = float(fn.split("_")[0])
		self.detail = TFLDetail(xml, epoch)

	def test_Platforms(self):
		self.assertEqual(len(self.detail.station.platforms), 2)
		self.assertEqual(self.detail.station.platforms[0].name, "Northbound - Platform 1")
		self.assertEqual(self.detail.station.platforms[0].trackCode, "TV6072")
		self.assertEqual(self.detail.station.platforms[1].trackCode, "TV6077")


	def test_Station(self):
		self.assertEqual(self.detail.station.name, "Blackhorse Road")
		self.assertEqual(self.detail.station.code, "BHR")
		self.assertEqual(self.detail.station.line, "V")
		self.assertEqual(self.detail.station.line_name, "Victoria Line")
		

class TestDetailTrains(unittest.TestCase):
	def setUp(self): 
		path = "./tests/fixtures/"
		fn = "1418383579.335227_Detail_V_Victoria_STK.xml"
		xml = open(path+fn).read()
		epoch = float(fn.split("_")[0])
		self.detail = TFLDetail(xml, epoch)

	def test_Trains(self):
		self.assertEqual(len(self.detail.trains), 11)
		self.assertEqual(self.detail.trains[0].lcid, "1067518")
		self.assertEqual(self.detail.trains[10].lcid, "1068894")

		self.assertEqual(self.detail.trains[0].trackCode, "TV6820_1")
		self.assertEqual(self.detail.trains[10].trackCode, "TV6945")
		
		