# สร้างลิสท์ของตัวเลขนำโชค4ตัว
# แล้วให้ผู้ใช้เสี่ยงโชคโดยกรอกตัวเลข 2 ตัว
# print True ถ้าตัวเลขที่ผู้ใช้เดาทั้ง2ตัว อยู่ในลิสท์เลขนำโชค
# print False ถ้ามีตัวใดตัวหนึ่งไม่อยู่ในลิสท์เลขนำโชค
# หลังจากนั้น นำตัวเลข2ตัวแรกในเลขนำโชคออก
# แล้วเพิ่มตัวเลขที่ผู้ใช้กรอกทั้ง2ตัว ไปเป็นเลขนำโชคแทน

lucky_numbers = [5,2,1,7]
n1 = int(input("เดาเลขที่1: "))
n2 = int(input("เดาเลขที่2: "))

print((n1 in lucky_numbers) and (n2 in lucky_numbers))

lucky_numbers = [lucky_numbers[2],lucky_numbers[3],n1,n2]

print(lucky_numbers)