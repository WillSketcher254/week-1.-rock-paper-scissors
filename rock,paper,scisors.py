import random

print('To quit press q, or write Quit')
quiting = False

while quiting == False:
    choices = ['rock','paper','scissors']
    rand = random.randint(0,2)
    comp = choices[rand]

    user = input('What is your choice ?\n')
    user = user.lower()

    if user == 'rock' or user == 'paper' or user == 'scissors':
        print(f'comp:{comp} user:{user}')
        if user == comp:
            print("It's a tie !!")
        elif user == 'rock' and comp == 'scissors':
            print('User wins !!')
        elif user == 'paper' and comp == 'rock':
            print('User wins !!')
        elif user == 'scissors' and comp == 'paper':
            print('User wins !!')
        else:
            print('Computer wins !!')
    elif user == 'q' or user == 'quit':
        print('Goodbye')
        quiting = True
    else:
        print('Please use a valid input\nOr correct your spelling')
