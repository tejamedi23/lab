num = int(input("Enter a decimal number: "))

binary = ""
n = num

while n > 0:
    r = n % 2
    binary = str(r) + binary
    n = n // 2

print("Binary equivalent =", binary)
