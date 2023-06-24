class Student():
    def __init__(self,name,score=0):
        self.name = name
        self.score = score

mike = Student("Mike")
mike.score = 80
print(mike.score)

