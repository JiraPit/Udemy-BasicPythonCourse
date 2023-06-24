class Bedroom:
    has_carpet = False

    def __init__(self):
        print("INIT!")

    def buy_carpet(self):
        print("ซื้อพรมแล้ว!!")
        self.has_carpet = True

johns_bedroom = Bedroom()

