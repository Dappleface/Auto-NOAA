from skyfield.api import load

stations_url = 'http://celestrak.com/NORAD/elements/noaa.txt'
satellites = load.tle(stations_url)
noaa15 = satellites[25338]
noaa18 = satellites[28654]
noaa19 = satellites[33591]

bluffton = Topos(nstopos, wetopos)
difference = noaa15 - bluffton
print('noaa15')
print(difference)
print('')
print('')
difference = noaa18 - bluffton
print('noaa18')
print(difference)
print('')
print('')
difference = noaa19 - bluffton
print('noaa19')
print(difference)