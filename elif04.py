
a=float(input("Masofani kiriting: "))

if 0<=a<1:
    print("Piyoda yuring: ")

elif 1<=a<=5:
    print("Velosiped yoki elektr skuter: ")

elif 5<a<=50:
    print("Avtobus yoki mashina: ")

elif 50<a:
    print("Poyezd yoki samalyot:")
    if 0>a:
        print("Masofa manfiy bo'la olmaydi.")