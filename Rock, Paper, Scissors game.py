import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


game_images = [rock,paper,scissors]

user_choice=int(float(input("Choose a number between 0, 1, 2. Where 0 is rock 1 is paper and 2 is scissors\n")))

if 0<=user_choice<=2:
    print(f"You chose{game_images[user_choice]}")
else:
    print("Please only type numbers between 0 and 2")
computer_choice=random.randint(0,2)
print(f"Computer choose {game_images[computer_choice]}")

if user_choice>computer_choice:
    print("You win")
elif user_choice==2 and computer_choice==0:
    print("You lose")
elif user_choice==computer_choice:
    print("It's a Draw")
elif computer_choice>user_choice:
    print("You lose")
