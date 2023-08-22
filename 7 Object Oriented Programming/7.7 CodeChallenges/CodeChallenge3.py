class Zoo:
    def __init__(self) -> None:
        self.__animal_list = []

    def add_animal(self,animal_name):
        self.__animal_list.append(animal_name)

    def print_animal_list(self):
        print(self.__animal_list)

dusit_zoo  = Zoo()

dusit_zoo.add_animal("เสือ")
dusit_zoo.add_animal("ยีราฟ")
dusit_zoo.add_animal("สิงโต")

dusit_zoo.__animal_list.remove("เสือ")