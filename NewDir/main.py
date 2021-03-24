def myfunc(a):
    lenght = len(a)
    for i in range(lenght):
        if i % 2 == 0:
            a = a[:i] + a[i].upper() + a[i + 1:]
        else:
            a = a[:i] + a[i].lower() + a[i + 1:]
    return a


#

# exercise 1
def showRes(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return min(a, b)
    else:
        return max(a, b)


# print(showRes(1, 3))


def crack_animal(animalOne, animalTwo):
    if animalOne[0].upper() == animalTwo[0].upper():
        return True
    else:
        return False


print(crack_animal("Lion", "Loki"))


def old_macdonald(a):
    a = a[0].upper() + a[1:3] + a[3].upper() + a[4:]
    return a


print(old_macdonald("mocadi"))
