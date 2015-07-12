import random
import sys

def sum_game():
    num1 = random.randint(1,101)
    num2 = random.randint(1,101)
    while True:
        print('%s + %s = ??' % (num1,num2))
        print('What\'s the sum?')
        ans = input()
        if ans.strip() == "":
            print('C\'mon.. you can do this!')
        else:
            i = int(ans)
            if i == num1+num2:
                print('Yay! You\'re smaht!')
                break
            elif i != num1+num2:
                print('Nope! Go back to school!')

def again():
    while True:
        print('Press enter to play again')
        input()
        sum_game()

sum_game()
again()
