#########################################################################
from random import*

Rock = '''   
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''


Paper = '''   
    _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''



Scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


images = [Rock ,Paper, Scissors]
user = int(input())
if user >=3 or user <0:
    print('you Typed an Invalid number.You loose!')
else:
    print(f'{images[user]}')
    
    computer = randint(0,2)
    index = images[computer]
    print(f'Computer choose {index}')

    if user == 0 and computer == 1:
        print('You Loose')
    elif user == 1 and computer == 0:
        print('You Won')
    elif user == 0 and computer == 2:
        print('You Won')
    elif user == 2 and computer == 0:
        print('You Loose')
    elif user == 1 and computer == 2:
        print('You Loose')
    elif user == 2 and computer == 1:
        print('You Won')
    elif user == computer:
        print('You draw')

























#############################################################################
from random import*

Rock = '''   
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''


Paper = '''   
    _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''



Scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user = input()

lists = [Rock ,Paper, Scissors]
index = randint(0,2)
computer = lists[index]

if user == 'Rock' and computer == Scissors:
    print(f'{Rock}\n{Scissors}','You Won')
    
elif user =='Scissors' and computer == Rock:
    print(f'{Scissors}\n{Rock}','You Loose')
    
elif user =='Rock' and computer == Paper:
    print(f'{Rock}\n{Paper}','You Loose')
    
elif user =='Paper' and computer == Rock:
    print(f'{Paper}\n{Rock}','You Won')
    
elif user =='Paper' and computer == Scissors:
    print(f'{Paper}\n{Scissors}','You Loose')
    
elif user =='Scissors' and computer == Paper:
    print(f'{Scissors}\n{Paper}','You Won')
else:
    if user =='Scissors' and computer == Scissors:
        print(f'{Scissors}\n{Scissors}','Game Draw')
    elif user =='Paper' and computer == Paper:
        print(f'{Paper}\n{Paper}','Game Draw')
    elif user =='Rock' and computer == Rock:
        print(f'{Rock}\n{Rock}','Game Draw')
