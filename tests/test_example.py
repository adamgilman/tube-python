
def test_TFLObject():
	'''
	Test implementation of TFL object

	>>> from tflTube import TFL
	>>> tfl = TFL()

	'''
	pass

def test_LinesStationMapping():
	'''
	Test that I can access stations and
		then subsequently the lines at statations and
		then subsequently the stations along those lines and
		then etc

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

	'''
	pass

def test_GetPlatformsAvailableAtStationsOnLine():
	'''
	Test that I can access the platforms that exist at 
	a station along a line
		: At Oxford Circus, on the Victoria line, 
			there is a northbound and southbound platform

	>>> from tflTube import TFL
	>>> tfl = TFL()
	>>> oxc = tfl.map.stations['OXC']
	>>> oxc
	<tflTube.TFLStation: Oxford Circus>

	>>> baker = tfl.map.lines['B']
	>>> baker
	<tflTube.TFLLine: Bakerloo>
	
	#>>> tfl.getPlatforms(oxc, baker)
	#[<tflTube.TFLPlatform: Southbound - Platform 3>, <tflTube.TFLPlatform: Northbound - Platform 4>]
	'''
	pass






