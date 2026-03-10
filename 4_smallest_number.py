a=int(input("Enter A: "))
b=int(input("Enter B: "))
c=int(input("Enter C: "))

if a<b and a<c:
    print("Smallest =",a)
elif b<c:
    print("Smallest =",b)
else:
    print("Smallest =",c)
