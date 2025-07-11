planet = {
    'name': 'Mars',
    'moons': 2
}
print(f'{planet["name"]} has {planet["moons"]} moon(s)')

planet['circumference (km)'] = {
    'polar': 6752,
    'equatorial': 6792
}
print(f'{planet["name"]} has a polar circumference of {planet["circumference (km)"]["polar"]}')

#------------------------------------------------------------------------------------------------

planet_moons = {
    'mercury': 0,
    'venus': 0,
    'earth': 1,
    'mars': 2,
    'jupiter': 79,
    'saturn': 82,
    'uranus': 27,
    'neptune': 14,
    'pluto': 5,
    'haumea': 2,
    'makemake': 1,
    'eris': 1
}

moons = planet_moons.values()
total_planets = len(planet_moons.keys())

print(moons)
print(total_planets)

total_moons = 0
for moon in moons:
    total_moons = total_moons + moon

average = total_moons / total_planets

print(f'Each planet has an average of {average} moons')