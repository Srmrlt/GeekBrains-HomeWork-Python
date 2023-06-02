class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass(self):
        road_mass = self._length * self._width * 0.5 * 25
        return road_mass


my_road = Road(1000, 3)
print(my_road.mass())
