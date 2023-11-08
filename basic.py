import numpy as np

x = 1
y = 2


def x_greater_than_y(x, y):
    if x > y:
        print("x er større enn y")
    else:
        print("x er ikke større enn y")


def input(x):
    print("Jeg fikk", x, "som input")


def square(x):
    return x*x


input("Hei")

print("2 i andre er", square(2))

i = 0
while i < 10:
    i += 1
    print(i)

min_liste = np.array([1, 2, 3, 4, 5])

start = 3
slutt = 11
step = 3

for i in range(start, slutt, step):
    print(i)

# { x  |  0 < x < 3, x heltall }  - mengdebygger
minliste = [x for x in range(10) if x < 3 and x > 0]
