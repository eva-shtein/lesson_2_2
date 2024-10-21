number_1 = input('Enter an integer: ')
number_2 = input('Enter an integer: ')
number_3 = input('Enter an integer: ')
if number_1 == number_2 and number_1 == number_3 and number_2 == number_3:
    print('third')
elif number_1 == number_2 or number_1 == number_3 or number_2 == number_3:
    print('second')
elif number_1 != number_2 and number_1 != number_3 and number_2 != number_3:
    print ('first')