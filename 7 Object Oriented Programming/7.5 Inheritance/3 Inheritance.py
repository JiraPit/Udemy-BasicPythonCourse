class Animal:
    def __init__(self,colour,legs_count):
        self.colour = colour
        self.legs_count = legs_count
    
    def move(self):
        print("ขยับ...ขยับ...")

class Snake(Animal):
    def __init__(self,fang_count,color):
        super().__init__(color,0)
        self.fang_count = fang_count
    
    def bite(self):
        print("งูฉก!")

my_snake = Snake(fang_count=2,color="grey");
print(my_snake.fang_count)
print(my_snake.colour)
print(my_snake.legs_count)
my_snake.move()
my_snake.bite()




