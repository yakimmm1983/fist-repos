
#
# import math
# def ploshad(a,b,r):
#     result = {}
#     areaCicle = math.pi*r**2
#     areaSquare = a*b
#     result.update({"Площадь квадрата": areaSquare})
#     result.update({"Площадь круга": areaCicle})
#     return result
#
# a=int(input("введите высоту прямоугольника"))
# b=int(input("введите ширину прямоугольника"))
# r=int(input("введите радиус круга"))
#
# for key,item in ploshad(a,b,r).items():
#     print(f"{key}: {item}")

import random

def getHealth():
    health = 100
    while True:
        pers1 = random.randint(1, 20)
        pers2 = random.randint(1, 20)
        if pers1 > pers2 :
            health = health - 20
        if health <= 0:
            print("здоровье закончилось")
            break
getHealth()

def delSecontElement(array:list):
    return array[::2]
print(delSecontElement([1,2,3,4,5,6,7,8,9]))
def fibonachi(n):
    if n == -2 or n == -3:
        return n
    return fibonachi(n-2)+fibonachi(n-1)
print(fibonachi(5))

import math
def Ploshad():
    sektor = int(input("колличество секторов"))
    circle = int(input("радиус круга"))

    return math.pi*circle**2/sektor

print(Ploshad())