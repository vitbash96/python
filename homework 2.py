# Ex.1
list1 = [12, 47.5, "sampletext", 5, False, None]
for n in range(0, len(list1)):
    print(type(list1[n]))

# Ex. 2
a = list(input('Enter some elements in the list (separated by space):').split())
b = a.copy()
n = 0
if len(a) % 2 == 0:
    while n < len(a) - 1:
        a[n] = b[n + 1]
        a[n + 1] = b[n]
        n += 2
else:
    while n < len(a) - 2:
        a[n] = b[n + 1]
        a[n + 1] = b[n]
        n += 2

print(a)

# Ex. 3
dict1 = {'Winter': (1, 2, 12), 'Spring': (3, 4, 5), 'Summer': (6, 7, 8), 'Autumn': (9, 10, 11)}
list1 = ['winter', 'winter', 'spring', 'spring', 'spring', 'summer', 'summer', 'summer', 'autumn', 'autumn', 'autumn',
         'winter']
# dictionary version
a = int(input("Enter the number of the month:"))
for n in dict1.keys():
    if a in dict1[n]:
        print(n)
# list version
a = int(input("Enter the number of the month:"))
print(list1[a])

# Ex. 4
list2 = list(input('Enter some words (separated by space):').split())
for n in range(0, len(list2)):
    print(f' {n + 1} {list2[n][:10]}')

# Ex. 5
list3 = [7, 5, 3, 3, 2]
p = None
while True:
    score = int(input("Enter your score:"))
    for n, num in enumerate(list3):
        if score > num:
            p = n
            break
    if p is None:
        list3.append(score)
    elif score == 0:
        list3.append(score)
    else:
        list3.insert(p, score)
    print(list3)

    y = input("Exit? y/n:")
    if y.lower == 'y':
      break
