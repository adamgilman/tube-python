tfl-tube-python
===============

Python object wrapper for TfL (Transport for London) TrackerNet information service


## What it does
lorem

## Requirements

# Usage
### Pythonic Tube Map
Explore the underground via a map of Python objects for each station and lines interlinked via the actual tube representation.

```python
>>> from tflTube import TFL
>>> tfl = TFL()
>>> tfl.map.lines
{'C': <tflTube.TFLLine: Central>, 'B': <tflTube.TFLLine: Bakerloo>, 'D': <tflTube.TFLLine: District>, 'H': <tflTube.TFLLine: Hammersmith & Circle>, 'J': <tflTube.TFLLine: Jubilee>, 'M': <tflTube.TFLLine: Metropolitan>, 'N': <tflTube.TFLLine: Nothern>, 'P': <tflTube.TFLLine: Piccadilly>, 'W': <tflTube.TFLLine: Waterloo & City>, 'V': <tflTube.TFLLine: Victoria>}
>>> tfl.map.lines['V']
<tflTube.TFLLine: Victoria>
>>> tfl.map.lines['V'].stations
{'VIC': <tflTube.TFLStation: Victoria>, 'WAL': <tflTube.TFLStation: Walthamstow Central>, 'PIM': <tflTube.TFLStation: Pimlico>, 'GPK': <tflTube.TFLStation: Green Park>, 'WST': <tflTube.TFLStation: Warren Street>, 'BRX': <tflTube.TFLStation: Brixton>, 'FPK': <tflTube.TFLStation: Finsbury Park>, 'STK': <tflTube.TFLStation: Stockwell>, 'KXX': <tflTube.TFLStation: King's Cross St Pancras>, 'TTH': <tflTube.TFLStation: Tottenham Hale>, 'HBY': <tflTube.TFLStation: Highbury and Islington>, 'VUX': <tflTube.TFLStation: Vauxhall>, 'BHR': <tflTube.TFLStation: Blackhorse Road>, 'SVS': <tflTube.TFLStation: Seven Sisters>, 'EUS': <tflTube.TFLStation: Euston>, 'OXC': <tflTube.TFLStation: Oxford Circus>}
>>> tfl.map.lines['V'].stations['VIC'].lines
{'H': <tflTube.TFLLine: Hammersmith & Circle>, 'D': <tflTube.TFLLine: District>, 'V': <tflTube.TFLLine: Victoria>}
```

### Train Predication Service 
See every train scheduled to arrive at every platform.

```
>>> tfl.map.stations['HBY'].trains
[]
```

Which is just a shortcut version of

```
>>> tfl.getPlatforms(self.tfl.map.stations['OXC'], self.tfl.map.lines['B']) 
```





