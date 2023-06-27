class Student():
    def __init__(self,name,score):
        self.name = name
        self.__score = score

    def print_score(self):
        print(self.__score)
    
mike = Student("Mike",80)
mike.print_score()



