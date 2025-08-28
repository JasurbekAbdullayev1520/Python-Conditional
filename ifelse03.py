
import os

fayl=input("Fayl nomini kiriting:")

if os.path.exists(fayl):
    print(f"Fayl {fayl} mavjut")

else:
    print(f"Fayl <{fayl}> topilmadi.")