import time


class TrafficLight:

    def __init__(self):
        self.__color = 'Red'

    def running(self):
        print(self.__color)
        time.sleep(7)
        self.__color = 'Yellow'
        print(self.__color)
        time.sleep(2)
        self.__color = 'Green'
        print(self.__color)
        time.sleep(3)


s1 = TrafficLight()
s1.running()
s2 = TrafficLight()
s2.running()
