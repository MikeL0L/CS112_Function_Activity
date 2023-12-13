def same_multiply():
    answer = num1 * num2 * num3
    print('Result is: ', answer)

def only_two_same_a():
    answer = num1 * num2 + num3 #a1
    print('Result is: ', answer)

def only_two_same_b():
    answer = num1 * num3 + num2 #b1
    print('Result is: ', answer)

def only_two_same_c():
    answer = num2 * num3 + num1 #c1
    print('Result is: ', answer)

def different_add():
    answer = num1 + num2 + num3
    print('Result is: ', answer)

while True:
    print()
    print('CS112 Functions Activity\nBy: Michael Andres S. Cabot')
    num1 = int(input('First Number: '))
    num2 = int(input('Second Number: '))
    num3 = int(input('Third Number: '))

    if num1 == num2 and num1 == num3 and num2 == num1 and num2 == num3 and num3 == num1 and num3 == num2:
        same_multiply()

    elif num1 == num2:
        only_two_same_a()

    elif num1 == num3:
        only_two_same_b()

    elif num2 == num3:
        only_two_same_c()

    elif num1 != num2 and num1 != num3 and num2 != num1 and num2 != num3 and num3 != num1 and num3 != num2:
        different_add()

    else:
        print('Error!');print()
        break
