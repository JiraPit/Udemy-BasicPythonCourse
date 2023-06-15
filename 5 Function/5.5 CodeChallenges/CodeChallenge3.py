# เขียนฟังก์ชั่นที่รับพารามิเตอร์เป็น List ของตัวเลขจำนวนเต็มกี่จำนวนก็ได้ 
# เพื่อกรองเอาเลขคี่ออก เก็บไว้แค่เลขคู่ แล้วคืนค่า List 
# ที่มีแต่เลขคู่นั้นออกมา แต่ถ้าไม่มีเลขคู่อยู่ในนั้นเลย 
# ให้คืนค่า String ว่า "ไม่พบเลขคู่"

def even_filter(input_list):
    even = []
    
    for i in input_list:
        if i%2==0:
            even.append(i)
    
    if len(even) == 0:
        return "ไม่พบเลขคู่"
    else:
        return even
    
print(even_filter([1,5,3]))