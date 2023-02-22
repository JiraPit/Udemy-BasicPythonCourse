class Student():
    def __init__(self,name,score=0):
        self.name = name
        self.__score = score
    
    def set_score(self,score):
        if score<=100 and score>=0:
            self.__score = score
    
    def get_score(self):
        return self.__score

mike = Student("Mike")
mike.set_score(80)
print(mike.get_score)