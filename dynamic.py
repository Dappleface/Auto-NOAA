from skyfield.api import Topos

boston = earth + Topos('42.3583 N', '71.0636 W')
astrometric = boston.at(t).observe(mars)
alt, az, d = astrometric.apparent().altaz()

print(alt)
print(az)