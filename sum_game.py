import random
import sys

def sum_game():
    num1 = random.randint(1,101)
    num2 = random.randint(1,101)
    while True:
        print('%s + %s = ??' % (num1,num2))
        print('What\'s the sum?')
        ans = input()
        i = int(ans)
        if i == num1+num2:
            print('Yay! You\'re smaht!')
            break
        elif i != num1+num2:
            print('Nope! Go back to school!')

def again():
    print('Press enter to play again')
    input()
    sum_game()
    again()

sum_game()
again()
