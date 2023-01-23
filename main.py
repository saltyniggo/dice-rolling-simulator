#first we import the random module for random number generation
import random

#then we set the range of values of a dice
d4min_val = 1
d4max_val = 4
d6min_val = 1
d6max_val = 6
d8min_val = 1
d8max_val = 8
d10min_val = 1
d10max_val = 10
d12min_val = 1
d12max_val = 12
d20min_val = 1
d20max_val = 20

#to loop the rolling through user input
roll_again = 'yes'

#here is the loop
while roll_again == 'yes' or roll_again == 'y':
    print('Which dice shall I role?')
    dice_choice = input('The D4, D6, D8, D10, D12 or D20 are possible')
    print('')
    if dice_choice == 'd4':
        print(random.randint(d4min_val, d4max_val))
    elif dice_choice == 'd6':
        print(random.randint(d6min_val, d6max_val))
    elif dice_choice == 'd8':
        print(random.randint(d8min_val, d8max_val))
    elif dice_choice == 'd10':
        print(random.randint(d10min_val, d10max_val))
    elif dice_choice == 'd12':
        print(random.randint(d12min_val, d12max_val))
    elif dice_choice == 'd20':
        print(random.randint(d20min_val, d20max_val))
    else:
        print('Have a nice time :)')
        quit()
