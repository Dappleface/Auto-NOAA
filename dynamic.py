from skyfield.api import Topos, load, now
ts = load.timescale()
t = ts.now()

stations_url = 'http://celestrak.com/NORAD/elements/noaa.txt'

def satload(satname):
    satellites = load.tle(stations_url)
    satellite = satellites[satname]
    days = t - satellite.epoch
    if abs(days) > 1:
        satellites = load.tle(stations_url, reload=True)
        satellite = satellites[satname]
        print('{:.3f} days away from epoch'.format(days))
    print(satellite)

def sattrack(satname):
    satellites = load.tle(stations_url)
    satellite = satellites[satname]
    geocentric = satellite.at(t)
    print(geocentric.position.km)
    subpoint = geocentric.subpoint()
    print('latitude: ', subpoint.latitude)
    print('longitude: ', subpoint.longitude)
    print('Elevation (m): ', int(subpoint.elevation.m))





def dms_to_dd(d, m, s):
    dd = d + float(m)/60 + float(s)/3600
    return dd
print("noaa-15 current location from current position:")
print("current direction W-E (latitude)")
print(dms_to_dd(-17, 33, 08.2))
print("current direction N-S (longiatude)")
print(dms_to_dd(-49, 32, 38.6))
#=======================================================================
print("=====================================")
print(r"""
          ooo
         / : \
        / o0o \
  _____"~~~~~~~"_____
  \+###|U * * U|###+/
   \...!(.>..<)!.../
    ^^^^o|   |o^^^^
#+=====}:^^^^^:{=====+#
 .____  .|!!!|.  ____.
 |#####:/" " "\:#####|
 |#####=|NO-AA|=#####|
 |#####>\_____/<#####|
  ^^^^^   | |   ^^^^^
          o o
 """)

print("=====================================")


print("satload:   ")
print()
satload('NOAA 15 [B]')
print()
satload('NOAA 18 [B]')
print()
satload('NOAA 19 [+]')
print()

print("print sat trak:   ")
print()
sattrack('NOAA 15 [B]')
print()
sattrack('NOAA 18 [B]')
print()
sattrack('NOAA 19 [+]')