class Bedroom:
    has_carpet = False

    def __init__(self,bedsize,door_color):
        self.bed_size = bedsize
        self.door_colour = door_color

    def buy_carpet(self):
        print("ซื้อพรมแล้ว!!")
        self.has_carpet = True


johns_bedroom = Bedroom(5,"Green")

print(johns_bedroom.bed_size)
print(johns_bedroom.door_colour)


