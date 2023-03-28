# ใช้โจทย์เดียวกับ CodeChalenge1
# แต่ให้ตรวจสอบก่อนว่า คะแนนที่กรอกเข้ามาไม่เกิน100 และไม่น้อยกว่า0

score = int(input("กรอกคะแนน: "))

if score >= 0 and score <= 100:
    if score >= 80:
        print("เกรดA")
    elif score >=70:
        print("เกรดB")
    elif score >= 60:
        print("เกรดC")
    elif score >= 50:
        print("เกรดD")
    else:
        print("เกรดF")   