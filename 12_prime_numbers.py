n=int(input("Enter limit: "))

for num in range(2,n+1):
    prime=True
    for i in range(2,num):
        if num%i==0:
            prime=False
    if prime:
        print(num)
