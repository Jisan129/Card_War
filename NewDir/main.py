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


# print(old_macdonald("mocadi"))


def groot(string):
    length = len(string)
    c = 0
    d = " "
    for i in range(0, length):
        if string[i] == ' ':
            c = c + 1
    return c


print(groot("My "))


def showList(*args):
    c = False
    temp = 0
    for i in args:
        if i == 3:
            temp = temp + 1
            if temp == 2:
                c = True
        else:
            temp = 0
    return c


print(showList(1, 3, 3))


def three_stooges(a):
    look = len(a)
    s = ""
    for i in range(look):
        for j in range(0, 3):
            s = s + a[i]
    return s


print(three_stooges("abc"))


def summer_camp(*args):
    sum = 0
    for i in args:
        if 6 <= i <= 9:
            continue
        else:
            sum += i

    print(sum)


summer_camp(1, 2, 6, 7, 9, 10)


def stack_learner(*args):
    stack = []
    a = 0
    statement = False
    for i in args:
        if i == 0:
            a = a + 1

        elif i == 7:

            if a == 2:
                statement = True
                a = a - 2

            else:
                statement = False

    return statement


print(stack_learner(0, 1, 2, 7))


def primeNumbers(limit):
    numbers = 0
    result = 0
    for i in range(2, limit + 1):
        temp = 0

        for j in range(2, i - 1):
            c = i % j
            if c == 0:
                temp = 1

        if temp == 0:
            result += 1

    return result


print(primeNumbers(100))





def print_big(letter):
    patterns = {1:'  *  ',2:' * * ',3:'*   *',4:'*****',5:'**** ',6:'   * ',7:' *   ',8:'*   * ',9:'*    '}
    alphabet = {'A':[1,2,4,3,3],'B':[5,3,5,3,5],'C':[4,9,9,9,4],'D':[5,3,3,3,5],'E':[4,9,4,9,4]}
    for pattern in alphabet[letter.upper()]:
        print(patterns[pattern])


print_big('B')














