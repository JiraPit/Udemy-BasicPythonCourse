class Bedroom:
    bed_size = 6
    door_colour = "white"
    has_carpet = False

    def buy_carpet(self):
        print("ซื้อพรมแล้ว!!")
        self.has_carpet = True


johns_bedroom = Bedroom()

print(johns_bedroom.has_carpet)

johns_bedroom.buy_carpet()
print(johns_bedroom.has_carpet)

