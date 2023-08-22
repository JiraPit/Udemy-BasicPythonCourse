# ต่อจาก 7.1 ให้สร้างคลาสใหม่ โดยถ่ายทอดมาจากคลาสของรถก่อนหน้านี้ 
# โดยคลาสใหม่นี้จะเป็นคลาสของรถบรรทุก 6ล้อ มีAttributeเพิ่มอีก1ตัว 
# ได้แก่น้ำหนักที่บรรทุกได้ และ Method เพิ่มอีก1ตัว ซึ่งมีพารามิเตอร์เป็นน้ำหนักสินค้าที่ต้องการจะบรรทุก
# แล้ว Print ออกมาว่าน้ำหนักเกินที่รถรับได้หรือไม่

class Car:
    def __init__(self,brand, type,wheel_count) -> None:
        self.brand = brand
        self.type = type
        self.wheel_count = wheel_count

    def print_information(self):
        print("รถคันนี้ ยี่ห้อ"+self.brand+" เป็น"+self.type+" "+str(self.wheel_count)+"ล้อ")

class PickUpTruck(Car):
    def __init__(self, brand, weight) -> None:
        self.weight = weight
        super().__init__(brand, "รถบรรทุก", 6)

    def check_weight(self,w):
        if w<=self.weight:
            print("บรรทุกได้")
        else:
            print("น้ำหนักเกิน")

p1 = PickUpTruck("Toyota",1)

p1.check_weight(2)