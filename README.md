tfl-tube-python
===============

Python object wrapper for TfL (Transport for London) TrackerNet information service

[![Build Status](https://travis-ci.org/adamgilman/tfl-tube-python.svg?branch=master)](https://travis-ci.org/adamgilman/tfl-tube-python)

# Usage
### Pythonic Tube Map
Explore the underground via a map of Python objects for each station and lines interlinked via the actual tube representation.

```python

	>>> from tflTube import TFL
	>>> tfl = TFL()
	>>> tfl.map.get(linecode='V')
	<tflTube.TFLLine: Victoria>

	>>> tfl.map.get(linecode='V').getStations()
	{'VIC': <tflTube.TFLStation: Victoria>, 'WAL': <tflTube.TFLStation: Walthamstow Central>, 'PIM': <tflTube.TFLStation: Pimlico>, 'GPK': <tflTube.TFLStation: Green Park>, 'WST': <tflTube.TFLStation: Warren Street>, 'BRX': <tflTube.TFLStation: Brixton>, 'FPK': <tflTube.TFLStation: Finsbury Park>, 'STK': <tflTube.TFLStation: Stockwell>, 'KXX': <tflTube.TFLStation: King's Cross St Pancras>, 'TTH': <tflTube.TFLStation: Tottenham Hale>, 'HBY': <tflTube.TFLStation: Highbury and Islington>, 'VUX': <tflTube.TFLStation: Vauxhall>, 'BHR': <tflTube.TFLStation: Blackhorse Road>, 'SVS': <tflTube.TFLStation: Seven Sisters>, 'EUS': <tflTube.TFLStation: Euston>, 'OXC': <tflTube.TFLStation: Oxford Circus>}

	>>> tfl.map.get(stationcode="OXC")
	<tflTube.TFLStation: Oxford Circus>
	
	>>> tfl.map.get(stationcode="OXC").getLines()
	{'C': <tflTube.TFLLine: Central>, 'B': <tflTube.TFLLine: Bakerloo>, 'V': <tflTube.TFLLine: Victoria>}


```
### Train Predication Service 
See every train scheduled to arrive at every platform, station or line.

```

	>>> tfl.map.get(linecode="B", stationcode="OXC").platforms
	{u'Northbound - Platform 4': <tflTube.TFLPlatform: Bakerloo Northbound - Platform 4 >, u'Southbound - Platform 3': <tflTube.TFLPlatform: Bakerloo Southbound - Platform 3 >}

	>>> tfl.map.get(linecode="B", stationcode="OXC").getAllTrains()
	{u'1020241': <tflTube.TFLTrain LCID(1020241) on Bakerloo Line at Approaching Paddington>, u'1019966': <tflTube.TFLTrain LCID(1019966) on Bakerloo Line at Between Regents Park and Oxford Circus>, u'1020119': <tflTube.TFLTrain LCID(1020119) on Bakerloo Line at At Embankment Platform 5>, u'1019579': <tflTube.TFLTrain LCID(1019579) on Bakerloo Line at Queen's Park North Sidings>, u'1020129': <tflTube.TFLTrain LCID(1020129) on Bakerloo Line at At Waterloo Platform 3>, u'1019713': <tflTube.TFLTrain LCID(1019713) on Bakerloo Line at At Queen's Park Platform 2>, u'1019521': <tflTube.TFLTrain LCID(1019521) on Bakerloo Line at At Marylebone Platform 2>, u'1019884': <tflTube.TFLTrain LCID(1019884) on Bakerloo Line at At Elephant & Castle Platform 3>}

	>>> tfl.map.get(linecode="V").getAllTrains()
	{u'1019265': <tflTube.TFLTrain LCID(1019265) on Victoria Line at Between Highbury & Islington and Kings Cross St. P>, u'1019894': <tflTube.TFLTrain LCID(1019894) on Victoria Line at At Brixton Platform 2>, u'1020196': <tflTube.TFLTrain LCID(1020196) on Victoria Line at At Victoria>, u'1018651': <tflTube.TFLTrain LCID(1018651) on Victoria Line at At Blackhorse Road>, u'1019837': <tflTube.TFLTrain LCID(1019837) on Victoria Line at Between Kings Cross St. Pancras and Highbury & Isl>, u'1018285': <tflTube.TFLTrain LCID(1018285) on Victoria Line at Between Seven Sisters and Finsbury Park>, u'1018931': <tflTube.TFLTrain LCID(1018931) on Victoria Line at Between Tottenham Hale and Blackhorse Road>, u'1019444': <tflTube.TFLTrain LCID(1019444) on Victoria Line at At Vauxhall>, u'1019373': <tflTube.TFLTrain LCID(1019373) on Victoria Line at Between Finsbury Park and Seven Sisters>, u'1016438': <tflTube.TFLTrain LCID(1016438) on Victoria Line at Between Oxford Circus and Warren Street>, u'1018584': <tflTube.TFLTrain LCID(1018584) on Victoria Line at Between Kings Cross St. Pancras and Euston>, u'1016265': <tflTube.TFLTrain LCID(1016265) on Victoria Line at Approaching Stockwell>, u'1019561': <tflTube.TFLTrain LCID(1019561) on Victoria Line at At Walthamstow Central>, u'1020270': <tflTube.TFLTrain LCID(1020270) on Victoria Line at Northumberland Park Depot Area>, u'1018676': <tflTube.TFLTrain LCID(1018676) on Victoria Line at Between Warren Street and Oxford Circus>, u'1018480': <tflTube.TFLTrain LCID(1018480) on Victoria Line at At Oxford Circus>, u'1017788': <tflTube.TFLTrain LCID(1017788) on Victoria Line at Between Pimlico and Victoria>, u'1020123': <tflTube.TFLTrain LCID(1020123) on Victoria Line at At Green Park>, u'1016226': <tflTube.TFLTrain LCID(1016226) on Victoria Line at Between Walthamstow Central and Blackhorse Road>, u'1015704': <tflTube.TFLTrain LCID(1015704) on Victoria Line at Departed Highbury & Islington>, u'1019728': <tflTube.TFLTrain LCID(1019728) on Victoria Line at At Seven Sisters Platform 5>, u'1016783': <tflTube.TFLTrain LCID(1016783) on Victoria Line at At Brixton Platform 1>, u'1019976': <tflTube.TFLTrain LCID(1019976) on Victoria Line at Between Finsbury Park and Highbury & Islington>, u'1018094': <tflTube.TFLTrain LCID(1018094) on Victoria Line at At Euston>, u'1019666': <tflTube.TFLTrain LCID(1019666) on Victoria Line at Between Pimlico and Vauxhall>, u'1016351': <tflTube.TFLTrain LCID(1016351) on Victoria Line at Departed Finsbury Park>, u'1018158': <tflTube.TFLTrain LCID(1018158) on Victoria Line at At Stockwell>, u'1017691': <tflTube.TFLTrain LCID(1017691) on Victoria Line at At Platform>}

	>>> tfl.map.get(stationcode="OXC").getAllTrains()
	{'trains': {u'1018651': <tflTube.TFLTrain LCID(1018651) on Victoria Line at Approaching Tottenham Hale>, u'1017788': <tflTube.TFLTrain LCID(1017788) on Victoria Line at At Victoria>, u'1019728': <tflTube.TFLTrain LCID(1019728) on Victoria Line at Between Seven Sisters and Finsbury Park>, u'1018285': <tflTube.TFLTrain LCID(1018285) on Victoria Line at At Finsbury Park>, u'1016783': <tflTube.TFLTrain LCID(1016783) on Victoria Line at Brixton Area>, u'1019976': <tflTube.TFLTrain LCID(1019976) on Victoria Line at At Highbury & Islington>, u'1019894': <tflTube.TFLTrain LCID(1019894) on Victoria Line at At Brixton Platform 2>, u'1019265': <tflTube.TFLTrain LCID(1019265) on Victoria Line at At Kings Cross St. Pancras>, u'1016226': <tflTube.TFLTrain LCID(1016226) on Victoria Line at At Walthamstow Central>, u'1019444': <tflTube.TFLTrain LCID(1019444) on Victoria Line at At Pimlico>, u'1016438': <tflTube.TFLTrain LCID(1016438) on Victoria Line at At Oxford Circus>, u'1018584': <tflTube.TFLTrain LCID(1018584) on Victoria Line at Between Warren Street and Euston>, u'1020123': <tflTube.TFLTrain LCID(1020123) on Victoria Line at Approaching Oxford Circus>, u'1019561': <tflTube.TFLTrain LCID(1019561) on Victoria Line at At Walthamstow Central>, u'1020270': <tflTube.TFLTrain LCID(1020270) on Victoria Line at Between Northumberland Park Depot and Seven Sisters>, u'1018158': <tflTube.TFLTrain LCID(1018158) on Victoria Line at Between Stockwell and Vauxhall>}}


```





