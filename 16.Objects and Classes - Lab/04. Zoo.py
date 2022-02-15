class Zoo:

    def __init__(self,zoo_name) -> None:
        self.__animals = 0
        self.name = zoo_name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self,species,name):
        if species in ['mammal','fish','bird']:
            if species == 'mammal':
                self.mammals.append(name)
            elif species == 'fish':
                self.fishes.append(name)
            else:
                self.birds.append(name)
            self.__animals += 1
        else:
            pass

    def get_info(self,species):
        if species in ['mammal','fish','bird']:
            if species == 'mammal':
                return f"Mammals in {self.name}: {', '.join(self.mammals)}\nTotal animals: {self.__animals}"
            elif species == 'fish':
                return f"Fishes in {self.name}: {', '.join(self.fishes)}\nTotal animals: {self.__animals}"
            else:
                return f"Birds in {self.name}: {', '.join(self.birds)}\nTotal animals: {self.__animals}"
        else:
            pass


zoo = Zoo(input())

for _ in range(int(input())):
    animal = input().split(' ')
    zoo.add_animal(animal[0],animal[1])

output = zoo.get_info(input())
print(output)