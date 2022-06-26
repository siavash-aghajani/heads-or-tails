import random 
again='y'
while again=='y':
    if random.random()>.5:
        print("heads")
    else:
        print('tails')

    again=input('again? (y/n): ')
