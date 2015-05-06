tube-python
===============

Python object wrapper for TfL (Transport for London) TrackerNet information service

[![Build Status](https://travis-ci.org/adamgilman/tube-python.svg?branch=master)](https://travis-ci.org/adamgilman/tube-python)

# Installation
```
pip install tube

```

# Usage
### Easy Access to Trains on the Underground
Quickly get all trains on tube lines and near stations

All trains near Kings Cross Underground Station

```python
>>> from tube import Tube
>>> tube = Tube()
>>> pprint( tube.getAllTrainsForStation("KXX") )
[<Tube.Train LCID(5877211) on Metropolitan Line at Between Baker Street and Great Portland Street>,
 <Tube.Train LCID(5584481) on Metropolitan Line at Farringdon Sidings>,
 <Tube.Train LCID(5877791) on Metropolitan Line at Left Upton Park>,
 <Tube.Train LCID(1198252) on Nothern Line at At Borough Platform 1>,
 <Tube.Train LCID(5872401) on Metropolitan Line at At Liverpool Street>,
 <Tube.Train LCID(5871481) on Piccadilly Line at At Gloucester Road Platform 5>,
 <Tube.Train LCID(5873101) on Metropolitan Line at Approaching Mansion House>,
 <Tube.Train LCID(1197862) on Nothern Line at Between Kennington and  Elephant and Castle>,
 <Tube.Train LCID(5873651) on Metropolitan Line at At Aldgate East Platform 1>,...]
```

All trains on the Victoria Line

```python
>>> pprint( tube.getAllTrainsForLine("V") )
[<Tube.Train LCID(5854901) on Victoria Line at At Euston>,
 <Tube.Train LCID(5858511) on Victoria Line at 0>,
 <Tube.Train LCID(3695661) on Victoria Line at Approaching Green Park>,
 <Tube.Train LCID(5851091) on Victoria Line at Approaching Finsbury Park>,
 <Tube.Train LCID(3739211) on Victoria Line at Between Vauxhall and Pimlico>,
 <Tube.Train LCID(3735331) on Victoria Line at Between Stockwell and Brixton>,
 <Tube.Train LCID(5867211) on Victoria Line at Between Tottenham Hale and Seven Sisters>,
 <Tube.Train LCID(5813041) on Victoria Line at Between Oxford Circus and Green Park>,
 <Tube.Train LCID(3734731) on Victoria Line at At Kings Cross St. Pancras>,
 <Tube.Train LCID(3757771) on Victoria Line at At Victoria>,...]
```

### Fully Pythonic Tube Map
Explore the underground via a map of Python objects for each station and lines interlinked via the actual tube representation.

```python

	>>> from tube import Tube
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



