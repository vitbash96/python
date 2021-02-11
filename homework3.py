# # Ex. 1
def mydivision(a, b):
    if b == 0:
        print("Denominator is 0!")
        quit()
    else:
        ans = a / b
    print(ans)


a = int(input("Enter a numerator:"))
b = int(input("Enter a denominator:"))
mydivision(a, b)


# # Ex. 2
from datetime import date
import re


def get_data(**db):
    print(f'First Name: {db.get("name")}, Surname: {db.get("surname")},'
          f' Year of Birth: {db.get("year")}, City: {db.get("city")},'
          f' E-mail: {db.get("email")}, Postcode: {db.get("postcode")}, Phone: {db.get("phone")}')


db = {'name': 'Vitalii', 'surname': 'Bashilov', 'year': '1996', 'city': 'Helsinki',
      'email': 'student@hanken.fi', 'postcode': '00160', 'phone': '0401112233', }
a = 0
while a != 3:
    a = int(input('Enter "1" to see the example, "2" - to input new info, "3" - print new info:'))
    if a == 1: get_data(**db)
    if a == 2:
        name = input('First name:')
        while name.isspace() or name == '' or name.isdigit():
            name = (input('Name is obligatory field. Please, enter a correct name:'))

        surname = input('Surname:')
        while surname.isspace() or surname == '' or surname.isdigit():
            surname = (input('Surname is obligatory field. Please, enter a correct surname:'))

        year = input('Year of Birth:')

        regex_year = re.compile(r'^(19|20)\d{2}$')
        F = regex_year.match(year)
        while F is None:
            year = input(f'Year should be between 1900 and {date.today().year} :')
            F = regex_year.match(year)

        city = input('Enter a city:')
        while city.isspace() or city.isdigit() or city == '':
            city = input('City cannot be empty or a number. Please, enter the city:')

        email = input('Enter E-mail:')
        regex = re.compile(r'^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$', re.IGNORECASE)
        F = regex.match(email)
        while F is None:
            email = input('Please, enter a correct E-mail:')
            F = regex.match(email)

        postcode = input('Enter a postcode:')
        while postcode.isspace() or postcode == "" or postcode.isdigit() == False:
            postcode = input('Enter a correct postcode:')

        phone = input('Enter a phone number:')
        while phone.isspace() or phone == "" or phone.isdigit() == False:
            phone = input('Enter a correct phone number:')

        userdata = {'name': name, 'surname': surname, 'year': year, 'city': city, 'email': email, 'postcode': postcode,
                    'phone': phone}
get_data(**userdata)

# Ex. 3
def my_func_addition(a, b, c):
    mylist = [a, b, c]
    for i in range(len(mylist)):
        try:
            if type(mylist[i]) != int:
                mylist[i] = float(mylist[i])
        except:
            print('ERROR')
            quit()
    mylist.sort(reverse=True)
    return mylist[0] + mylist[1]


uinput = input('Enter 3 numbers separated by space').split()
print(my_func_addition(*uinput))

# Ex. 4
def my_exponentiation(x, y):
    for i in range(abs(y)-1):
        x = x * abs(y)
    return 1 / x


a = input('input one positive number and one negative integer separated by space:').split()
if len(a) > 2:
    print('incorrect input')
    quit()
try:
    if float(a[0]) <= 0:
        print('First number is not positive')
    else:
        a[0] = float(a[0])
except:
    print('Incorrect input')
    quit()
try:
    if int(a[1]) > 0:
        print('Second number is positive')
        quit()
    else:
        a[1] = int(a[1])
except:
    print('incorrect input')
    quit()
print(my_exponentiation(a[0], a[1]))

# Ex. 5
def my_sum(*a):
    summa = 0
    for i in range(len(a)):
        summa += a[i]
    return summa


sum1 = 0
while True:
    a = input('input some numbers separated by space, "q" - exit:').lower().split()

    if a.count('q') > 0:
        if a.index('q') == 0:
            print("Exit")
            break
        else:
            try: ### здесь должно удалять "q" из вектора и считать сумму остальных чисел, но не работает
                stop_index = a.index('q')
                a = a[:stop_index]
                sum1 += (my_sum(*a))
                print(sum1)
                break
            except:
                quit()
    for i in range(len(a)):
        try:
            a[i] = float(a[i])
        except:
            print("Incorrect input")
            quit()

    sum1 += (my_sum(*a))
    print(sum1)
# Ex. 6

def int_func(word):
    if not word.isalpha():
        raise ValueError(f'Input "{word}" is incorrect ')
    return word.capitalize()


try:
    words = input('input some words separated by space:').lower().split()
except:
    print(ValueError('Incorrect input'))
    quit()
print(' '.join([int_func(i) for i in words]))
