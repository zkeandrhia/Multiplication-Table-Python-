#multiplication table
num = int(input("Multiplication using value?"))

for x in range (1, num+1):
    multiplication = num * x
    print(f'{num} * {x} = {multiplication}')
for y in range (num-1, 11):
   print(f'{num} * {y} = {num * y}')