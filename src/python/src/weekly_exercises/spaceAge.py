#                               Introduction
#
# The year is 2525 and you've just embarked on a journey to visit all planets in
# the Solar System (Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus and
# Neptune). The first stop is Mercury, where customs require you to fill out a
# form (bureaucracy is apparently not Earth-specific). As you hand over the form
# to the customs officer, they scrutinize it and frown. "Do you really expect me
# to believe you're just 50 years old? You must be closer to 200 years old!"
#
# Amused, you wait for the customs officer to start laughing, but they appear to
# be dead serious. You realize that you've entered your age in Earth years, but
# the officer expected it in Mercury years! As Mercury's orbital period around
# the sun is significantly shorter than Earth, you're actually a lot older in
# Mercury years. After some quick calculations, you're able to provide your age
# in Mercury Years. The customs officer smiles, satisfied, and waves you
# through. You make a mental note to pre-calculate your planet-specific age
# before future customs checks, to avoid such mix-ups.
#
#   Note
#
# If you're wondering why Pluto didn't make the cut, go watch this YouTube
# video.
#
#   Instructions
#
# Given an age in seconds, calculate how old someone would be on a planet in our
# Solar System.
#
# One Earth year equals 365.25 Earth days, or 31,557,600 seconds. If you were
# told someone was 1,000,000,000 seconds old, their age would be 31.69
# Earth-years.
#
# For the other planets, you have to account for their orbital period in Earth
# Years:
#
#   Planet	    Orbital period in Earth Years
#   Mercury	    0.2408467
#   Venus	    0.61519726
#   Earth	    1.0
#   Mars	    1.8808158
#   Jupiter	    11.862615
#   Saturn	    29.447498
#   Uranus	    84.016846
#   Neptune	    164.79132
#
#   Note
#
# The actual length of one complete orbit of the Earth around the sun is closer
# to 365.256 days (1 sidereal year). The Gregorian calendar has, on average,
# 365.2425 days. While not entirely accurate, 365.25 is the value used in this
# exercise. See Year on Wikipedia for more ways to measure a year.
#
# For the Python track, this exercise asks you to create a SpaceAge class
# (classes) that includes methods for all the planets of the solar system.
# Methods should follow the naming convention on_<planet name>.
#
# Each method should return the age ("on" that planet) in years, rounded to two
# decimal places:
#
#   #creating an instance with one billion seconds, and calling .on_earth().
#   >>> SpaceAge(1000000000).on_earth()
#
#   #This is one billion seconds on Earth in years
#   31.69
#
# For more information on constructing and using classes, see:
#
#   - A First Look at Classes from the Python documentation.
#   - A Word About names and Objects from the Python documentation.
#   - Objects, values, and types in the Python data model documentation.
#   - What is a Class? from Trey Hunners Python Morsels website.
#
# References:
#
# - https://exercism.org/tracks/python/exercises/space-age
# - https://pine.fm/LearnToProgram/?Chapter=01
#


from typing import overload


class SpaceAge:
    PLANETS = {
        "Mercury": 0.2408467,
        "Venus": 0.61519726,
        "Earth": 1.0,
        "Mars": 1.8808158,
        "Jupiter": 11.862615,
        "Saturn": 29.447498,
        "Uranus": 84.016846,
        "Neptune": 164.79132,
    }

    def __init__(self, seconds: int) -> None:
        self.__seconds__ = seconds
        self.__init_planets__()

    @overload
    def on_mercury(self) -> float: ...
    @overload
    def on_venus(self) -> float: ...
    @overload
    def on_earth(self) -> float: ...
    @overload
    def on_mars(self) -> float: ...
    @overload
    def on_jupiter(self) -> float: ...
    @overload
    def on_saturn(self) -> float: ...
    @overload
    def on_uranus(self) -> float: ...
    @overload
    def on_neptune(self) -> float: ...

    def __init_planets__(self) -> None:
        for planet, orbital_period in self.PLANETS.items():
            setattr(
                self,
                f"on_{planet.lower()}",
                lambda orbital_period=orbital_period: round(
                    self.__seconds__ / 31557600 / orbital_period, 2
                ),
            )
