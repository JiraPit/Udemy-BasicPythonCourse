# เขียนฟังก์ชั่นที่รับพารามิเตอร์เป็น ตัวเลข2ตัว แล้วคืนค่าเป็น List ที่มีสมาชิก4ตัว ดังนี้
# ตัวเลขที่1 + ตัวเลขที่2
# ตัวเลขที่1 - ตัวเลขที่2
# ตัวเลขที่1 x ตัวเลขที่2
# ตัวเลขที่1 ÷ ตัวเลขที่2

def operations(number1,number2):
    return [
        number1 + number2,
        number1 - number2,
        number1 * number2,
        number1 / number2
        ]