def is_armstrong(n):
    digits =str(n)
    power =len(digits)
    total =sum(int(digit) **power for digit in digits)
    return total==n
num=153
if is_armstrong(num):
    print(f"{num} is an armstrong number")
else:
    print(f"{num} is not armstrong number")