class Bedroom:
    has_carpet = False

    def __init__(self,b):
        self.bed_size = b

    def buy_carpet(self):
        print("ซื้อพรมแล้ว!!")
        self.has_carpet = True


johns_bedroom = Bedroom(5)
jims_bedroom = Bedroom(3)

print(johns_bedroom.bed_size)
print(jims_bedroom.bed_size)


