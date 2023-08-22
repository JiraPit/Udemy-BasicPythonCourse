# สร้างคลาสของรถยนต์ขึ้นมา โดยประกอบไปด้วย Attribute 3 ตัว ได้แก่ ยี่ห้อ ชนิด และจำนวนล้อ
# และมี Method 1 ตัว ซึ่งจะ Print ข้อมูลทั้งหมดออกมา เช่น "รถคันนี้ยี่ห้อฮอนด้า เป็นซีดาน 4ล้อ"

class Car:
    def __init__(self,brand, type,wheel_count) -> None:
        self.brand = brand
        self.type = type
        self.wheel_count = wheel_count

    def print_information(self):
        print("รถคันนี้ ยี่ห้อ"+self.brand+" เป็น"+self.type+" "+str(self.wheel_count)+"ล้อ")

honda_car = Car("Honda","SUV",4)

honda_car.print_information()