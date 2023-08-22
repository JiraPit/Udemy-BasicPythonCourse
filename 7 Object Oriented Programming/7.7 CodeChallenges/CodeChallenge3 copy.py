class Zoo:
    def __init__(self) -> None:
        self.animal_list = []

dusit_zoo  = Zoo()

dusit_zoo.animal_list.append("เสือ")
dusit_zoo.animal_list.append("ยีราฟ")

dusit_zoo.animal_list.remove("เสือ")

print(dusit_zoo.animal_list)

