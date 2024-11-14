
from random import randint

list = []
listA = []
listB = []
listC = []

for i in range(20):
    num = randint(1,100)

    list.append(num)

for i in list:
    if i <= 30:
        listA.append(i)
    elif i >= 31 and i <= 69:
        listB.append(i)
    else:
        listC.append(i)

print(list )
print(listA )
print(listB )
print(listC )
