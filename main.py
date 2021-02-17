def planets(x):
    planet = [ "mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune"]
    for i in range(0, len(x)):
        if x == planet[i -1]:
            return i

    return  x +" " "is not a planet"
print(planets("russia"))

