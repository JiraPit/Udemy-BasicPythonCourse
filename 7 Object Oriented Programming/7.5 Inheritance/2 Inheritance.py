class Animal:
    def __init__(self,colour,legs_count):
        self.colour = colour
        self.legs_count = legs_count
    
    def move(self):
        print("ขยับ...ขยับ...")

class Snake(Animal):
    def __init__(self,fang_count):
        super().__init__("green",0)
        self.fang_count = fang_count
    
    def bite(self):
        print("งูฉก!")

my_snake = Snake(fang_count=2);
print(my_snake.fang_count)
print(my_snake.colour)
print(my_snake.legs_count)
my_snake.move()
my_snake.bite()


