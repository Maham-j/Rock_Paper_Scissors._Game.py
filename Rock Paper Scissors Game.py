from random import randint

# Define the images for Rock, Paper, and Scissors
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

# Get user input for their choice (Rock, Paper, or Scissors)
user = input("Enter your choice (Rock, Paper, Scissors): ")

# List of images and their corresponding choices
images = [Rock, Paper, Scissors]

# Generate a random index to simulate computer's choice
index = randint(0, 2)
computer_choice = images[index]

# Determine the game outcome based on user's choice and computer's choice
if user == 'Rock' and computer_choice == Scissors:
    print(f'{Rock}\n{Scissors}', 'You Won')
    
elif user == 'Scissors' and computer_choice == Rock:
    print(f'{Scissors}\n{Rock}', 'You Loose')
    
elif user == 'Rock' and computer_choice == Paper:
    print(f'{Rock}\n{Paper}', 'You Loose')
    
elif user == 'Paper' and computer_choice == Rock:
    print(f'{Paper}\n{Rock}', 'You Won')
    
elif user == 'Paper' and computer_choice == Scissors:
    print(f'{Paper}\n{Scissors}', 'You Loose')
    
elif user == 'Scissors' and computer_choice == Paper:
    print(f'{Scissors}\n{Paper}', 'You Won')
else:
    # Handle the case of a draw
    if user == computer_choice:
        print(f'{user}\n{computer_choice}', 'Game Draw')
