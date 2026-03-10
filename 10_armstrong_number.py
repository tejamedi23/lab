num=int(input("Enter number: "))
temp=num
s=0

while temp>0:
    digit=temp%10
    s+=digit**3
    temp//=10

if s==num:
    print("Armstrong")
else:
    print("Not Armstrong")
