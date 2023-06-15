class Bedroom:
    def __init__(self,b,d):
        self.bed_size = b
        self.door_colour = d
        self.has_carpet = False

    def buy_carpet(self):
        print("ซื้อพรมแล้ว!!")
        self.has_carpet = True


johns_bedroom = Bedroom(5,"black")

print(johns_bedroom.bed_size)
print(johns_bedroom.door_colour)

