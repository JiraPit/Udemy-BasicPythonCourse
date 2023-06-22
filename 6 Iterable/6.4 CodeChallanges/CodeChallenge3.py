# ให้ผู้ใช้กรอกตัวเลขเพื่อมาเก็บไว้ใน List L1 ไปเรื่อยๆจนกว่าผู้ใช้จะพิมพ์เลข0 
# จากนั้น ใช้ List Slicing เพื่อแบ่งครึ่ง List L1 ให้เป็น 2 List ที่เท่ากัน

list1 = []

while True:
    number = int(input("กรอกตัวเลข: "))
    if number == 0:
        break
    else:
        list1.append(number)

length = len(list1)
length = length/2

print(list1[:int(length)])
print(list1[int(length):])
