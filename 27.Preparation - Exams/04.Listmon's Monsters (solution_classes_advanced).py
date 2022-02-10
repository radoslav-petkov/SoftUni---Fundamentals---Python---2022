from abc import ABC, abstractmethod, ABCMeta
import sys

class BaseMonster(ABC):
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, name, number, strength, ugliness):
        self.name = name
        self.number = number
        self.strength = strength
        self.ugliness = ugliness

class Hydralisk(BaseMonster):
    def __init__(self, name, number, strength, ugliness, range):
        BaseMonster.__init__(self, name, number, strength, ugliness)
        self.range = self.set_range(range)

    def set_range(self, range):
        if not isinstance(range, str):
            raise Exception('Range must be string')
        return range

class Zergling(BaseMonster):
    def __init__(self, name, number, strength, ugliness, speed):
        BaseMonster.__init__(self, name, number, strength, ugliness)
        self.speed = self.set_speed(speed)

    def set_speed(self, speed):
        if not isinstance(speed, int):
            raise Exception('Speed must be integer')
        return speed

monsters = []

data = input()

while not  data == 'stopAddingArmy':
    try:
        monster = eval(data)
        monsters.append(monster)
    except Exception:
        print(sys.exc_info()[1])
    data = input()


overallspeed = sum([z.speed for z in list(filter(lambda x: isinstance(x, Zergling), monsters))])
overallstrength = sum([s.strength for s in monsters])
print(f'Overall speed of army: {overallspeed}')
print(f'Overall stength: {overallstrength}')
zerglings = len([z for z in list(filter(lambda x: isinstance(x, Zergling), monsters))])
hydralisks = len([z for z in list(filter(lambda x: isinstance(x, Hydralisk), monsters))])
print(f'Hydralisk: {hydralisks}; Zergling: {zerglings}')