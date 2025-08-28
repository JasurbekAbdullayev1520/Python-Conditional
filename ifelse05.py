
a = input("Email manzilni kiriting: ")

if "@" in a and (a.endswith(".com") or a.endswith(".net") or a.endswith(".org")):
    print("Email qabul qilindi")
else:
    print("Email noto'g'ri formatda")
