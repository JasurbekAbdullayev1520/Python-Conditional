
a=float(input("1-sonni kiriting:"))

b=float(input("2-sonni kiriting"))

c=input("amal:")

if c=='-':
    print(a-b)

elif c=='+':
    print(a+b)

elif c=='*':
    print(a*b)

elif c=='/':
    print(a/b)

    if a==0 or b==0:
        print( "0 ga bo'linmaydi")

else:
    print("Bunday son yo'q")

