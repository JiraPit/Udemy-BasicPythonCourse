def calculate_bmi(h, w):
    h = h/100
    bmi = w/(h**2)
    return bmi

my_bmi = calculate_bmi(174,52)

print(my_bmi)



