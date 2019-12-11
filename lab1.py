import random

def filling_list(size):
    list = []
    for i in range(size):
        list.append(random.randint(1, 50))
    return list

def sum_list(list):
    sum = 0
    for x in list:
        sum += x
    return sum

if __name__ == '__main__':
    n = int(input("Enter size of list: "))
    list = filling_list(n)
    sum = sum_list(list)
    average = sum / n
    print("Sum = " + str(sum) + "\naverage = " + str(average))