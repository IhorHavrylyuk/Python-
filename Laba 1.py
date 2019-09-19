import random

list1 = []
x=int(input("введіть кількысть елементів списку: "))
for i in range(0,x):
    list1.append(random.randint(1,50))
print(list1)
sum = 0
for i in list1:
    sum +=i
ser=sum/x
print("Сума: ",sum,"\t","Середнє значення:",ser)
