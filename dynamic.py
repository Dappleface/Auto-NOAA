from skyfield.api import *

planets = load('de421.bsp')
earth, mars = planets['earth'], planets['mars']

ts = load.timescale()
t = ts.now()
position = earth.at(t).observe(mars)
ra, dec, distance = position.radec()

print(ra)
print(dec)
print(distance)

print("Az +EL")

boston = earth + Topos('42.3583 N', '71.0636 W')
astrometric = boston.at(t).observe(mars)
alt, az, d = astrometric.apparent().altaz()

print(alt)
print(az)