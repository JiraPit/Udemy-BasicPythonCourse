# เขียนโปรแกรมต่อจาก ฟังก์ชั่นในข้อ 5.1 โดยนำ List ที่คืนค่ามา Print ทีละตัว เช่น
# " 2 + 4 = 6 "
# " 2 - 4 = -2 "
# " 2 * 4 = 8 "
# " 2 ÷ 4 = 0.5 "
# *สมมติว่าตัวเลข2ตัวเป็น 2 และ 4

n1 = 5
n2 = 20

op = ["+","-","*","/"]

def operations(number1,number2):
    return [
        number1 + number2,
        number1 - number2,
        number1 * number2,
        number1 / number2
        ]

results = operations(n1,n2)

for r in range(0,4):
    print(n1,op[r],n2," = ",results[r])