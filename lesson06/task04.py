class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Car {self.name} start with speed {self.speed}')

    def stop(self):
        print(f'Stopped by police: {self.is_police}')

    def turn(self, direction):
        print(f'{self.color} car turn {direction}')

    def show_speed(self):
        print(f'Car speed {self.speed}')


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print(f'High speed!!!')


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print(f'High speed!!!')


fr = Car(100, 'Red', 'BMW', False)
fr.go()
fr.stop()
fr.turn('Left')
fr.show_speed()
