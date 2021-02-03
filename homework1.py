# Ex.1
numeric = 12345
text = 'some text'
string1 = 'some numbers: %s' % numeric
string2 = 'some text: %s' % text
print(string1, string2, sep='\n')
# Ex.2
time = int(input("Input time in seconds:"))
h = time // 3600
m = time // 60 - h * 60
sec = time % 3600 - m * 60
print(f'{h}:{m}:{sec}')
# Ex.3
number1 = int(input("Input a positive integer"))
temp = f'{number1}{number1}'
a2 = int(temp)
temp = f'{number1}{number1}{number1}'
a3 = int(temp)
print(f'{number1 + a2 + a3}')
# Ex.4 Alternative solution
number2 = (input("Input a positive integer"))
print(max(number2))
# Ex. 4
number2 = int(input("Input an integer:"))
out = number2 % 10
number2 = number2 // 10
while number2 > 0:
    if number2 % 10 > out:
        out = number2 % 10
    number2 = number2 // 10
print(out)
# Ex. 5
revenue = int(input("Enter revenue:"))
costs = int(input("Enter costs:"))
if revenue > costs:
    print(f'Profit margin is: {(revenue - costs) / revenue}')
    humres = int(input("Enter a number of employees:"))
    print(f'Profit per employee: {(revenue - costs) / humres * 100}%')
elif revenue == costs:
    print("Break-even point")
else:
    print("It's a loss!")
# Ex. 6
a = int(input("Enter the distance for the 1st day, km:"))
b = int(input("Enter a goal, km:"))
day = 1
while a < b:
    a = 1.1 * a
    day = day + 1
print(day)
