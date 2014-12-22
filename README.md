tube-python
===============

Python object wrapper for TfL (Transport for London) TrackerNet information service

[![Build Status](https://travis-ci.org/adamgilman/tfl-tube-python.svg?branch=master)](https://travis-ci.org/adamgilman/tfl-tube-python)

# Usage
### Pythonic Tube Map
Explore the underground via a map of Python objects for each station and lines interlinked via the actual tube representation.

```python

	>>> from tubeAPI import Tube
	>>> tube = Tube()
	>>> tube.map.get(linecode='V')
	<Tube.Line: Victoria>

	>>> tube.map.get(linecode='V').getStations()
	{'VIC': <Tube.Station: Victoria>, 'WAL': <Tube.Station: Walthamstow Central>, 'PIM': <Tube.Station: Pimlico>, 'GPK': <Tube.Station: Green Park>, 'WST': <Tube.Station: Warren Street>, 'BRX': <Tube.Station: Brixton>, 'FPK': <Tube.Station: Finsbury Park>, 'STK': <Tube.Station: Stockwell>, 'KXX': <Tube.Station: King's Cross St Pancras>, 'TTH': <Tube.Station: Tottenham Hale>, 'HBY': <Tube.Station: Highbury and Islington>, 'VUX': <Tube.Station: Vauxhall>, 'BHR': <Tube.Station: Blackhorse Road>, 'SVS': <Tube.Station: Seven Sisters>, 'EUS': <Tube.Station: Euston>, 'OXC': <Tube.Station: Oxford Circus>}

	>>> tube.map.get(stationcode="OXC")
	<Tube.Station: Oxford Circus>
	
	>>> tube.map.get(stationcode="OXC").getLines()
	{'C': <Tube.Line: Central>, 'B': <Tube.Line: Bakerloo>, 'V': <Tube.Line: Victoria>}


```
### Train Predication Service 
See every train scheduled to arrive at every platform, station or line.

```

	>>> tube.map.get(linecode="B", stationcode="OXC").platforms
	{u'Northbound - Platform 4': <Tube.Platform: Bakerloo Northbound - Platform 4 >, u'Southbound - Platform 3': <Tube.Platform: Bakerloo Southbound - Platform 3 >}

	>>> tube.map.get(linecode="B", stationcode="OXC").getAllTrains()
	{u'1030085': <Tube.Train LCID(1030085) on Bakerloo Line at Approaching Waterloo>, u'1031201': <Tube.Train LCID(1031201) on Bakerloo Line at Approaching Elephant & Castle>, u'1029910': <Tube.Train LCID(1029910) on Bakerloo Line at At Regents Park Platform 2>, u'1032071': <Tube.Train LCID(1032071) on Bakerloo Line at Left Embankment>, u'1029021': <Tube.Train LCID(1029021) on Bakerloo Line at Left Marylebone>, u'1031368': <Tube.Train LCID(1031368) on Bakerloo Line at Queen's Park North Sidings>, u'1029809': <Tube.Train LCID(1029809) on Bakerloo Line at Queen's Park North Sidings>, u'1030617': <Tube.Train LCID(1030617) on Bakerloo Line at Left Maida Vale>, u'1032246': <Tube.Train LCID(1032246) on Bakerloo Line at Approaching Queen's Park>, u'1029757': <Tube.Train LCID(1029757) on Bakerloo Line at Between Queen's Park and Kilburn Park>, u'1032055': <Tube.Train LCID(1032055) on Bakerloo Line at At Paddington Platform 4>, u'1031478': <Tube.Train LCID(1031478) on Bakerloo Line at At Platform>, u'1030347': <Tube.Train LCID(1030347) on Bakerloo Line at At Elephant & Castle Platform 3>, u'1029382': <Tube.Train LCID(1029382) on Bakerloo Line at At Piccadilly Circus Platform 1>, u'1029109': <Tube.Train LCID(1029109) on Bakerloo Line at At Willesden Junction Platform 1>}

	>>> tube.map.get(linecode="V").getAllTrains()
{u'1032146': <Tube.Train LCID(1032146) on Victoria Line at At Pimlico>, u'1027885': <Tube.Train LCID(1027885) on Victoria Line at At Platform>, u'1029333': <Tube.Train LCID(1029333) on Victoria Line at At Kings Cross St. Pancras>, u'1030100': <Tube.Train LCID(1030100) on Victoria Line at At Highbury & Islington>, u'1030219': <Tube.Train LCID(1030219) on Victoria Line at Between Kings Cross St. Pancras and Highbury & Isl>, u'1030324': <Tube.Train LCID(1030324) on Victoria Line at Departed Vauxhall>, u'1031638': <Tube.Train LCID(1031638) on Victoria Line at At Finsbury Park>, u'1029114': <Tube.Train LCID(1029114) on Victoria Line at At Blackhorse Road>, u'1029796': <Tube.Train LCID(1029796) on Victoria Line at Departed Warren Street>, u'1031881': <Tube.Train LCID(1031881) on Victoria Line at Between Victoria and Pimlico>, u'1029869': <Tube.Train LCID(1029869) on Victoria Line at At Brixton Platform 1>, u'1029892': <Tube.Train LCID(1029892) on Victoria Line at At Seven Sisters Platform 5>, u'1032228': <Tube.Train LCID(1032228) on Victoria Line at Between Oxford Circus and Green Park>, u'1029173': <Tube.Train LCID(1029173) on Victoria Line at Between Stockwell and Brixton>, u'1029614': <Tube.Train LCID(1029614) on Victoria Line at Between Highbury & Islington and Finsbury Park>, u'1028128': <Tube.Train LCID(1028128) on Victoria Line at At Victoria>, u'1029917': <Tube.Train LCID(1029917) on Victoria Line at Between Warren Street and Euston>, u'1030278': <Tube.Train LCID(1030278) on Victoria Line at At Platform>, u'1029515': <Tube.Train LCID(1029515) on Victoria Line at At Walthamstow Central>, u'1030241': <Tube.Train LCID(1030241) on Victoria Line at Between Finsbury Park and Seven Sisters>, u'1029235': <Tube.Train LCID(1029235) on Victoria Line at Approaching Euston>, u'1025823': <Tube.Train LCID(1025823) on Victoria Line at At Highbury & Islington>, u'1030168': <Tube.Train LCID(1030168) on Victoria Line at At Platform>, u'1030194': <Tube.Train LCID(1030194) on Victoria Line at Between Seven Sisters and Finsbury Park>, u'1029740': <Tube.Train LCID(1029740) on Victoria Line at Between Tottenham Hale and Blackhorse Road>, u'1029200': <Tube.Train LCID(1029200) on Victoria Line at Between Seven Sisters and Finsbury Park>, u'1031053': <Tube.Train LCID(1031053) on Victoria Line at At Green Park>}

	>>> tube.map.get(stationcode="OXC").getAllTrains()
	{'trains': {u'1032146': <Tube.Train LCID(1032146) on Victoria Line at Between Pimlico and Victoria>, u'1029173': <Tube.Train LCID(1029173) on Victoria Line at At Brixton Platform 2>, u'1029333': <Tube.Train LCID(1029333) on Victoria Line at At Kings Cross St. Pancras>, u'1031053': <Tube.Train LCID(1031053) on Victoria Line at Between Green Park and Oxford Circus>, u'1030100': <Tube.Train LCID(1030100) on Victoria Line at Between Highbury & Islington and Kings Cross St. P>, u'1029917': <Tube.Train LCID(1029917) on Victoria Line at At Warren Street>, u'1028128': <Tube.Train LCID(1028128) on Victoria Line at Between Victoria and Green Park>, u'1029114': <Tube.Train LCID(1029114) on Victoria Line at Between Tottenham Hale and Blackhorse Road>, u'1029515': <Tube.Train LCID(1029515) on Victoria Line at At Walthamstow Central>, u'1029235': <Tube.Train LCID(1029235) on Victoria Line at At Euston>, u'1030194': <Tube.Train LCID(1030194) on Victoria Line at Between Seven Sisters and Finsbury Park>, u'1029869': <Tube.Train LCID(1029869) on Victoria Line at At Brixton Platform 1>, u'1029200': <Tube.Train LCID(1029200) on Victoria Line at At Finsbury Park>, u'1029892': <Tube.Train LCID(1029892) on Victoria Line at At Seven Sisters Platform 5>}}

```





