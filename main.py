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

#Write your code below this line 👇

arr = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice > 2 or user_choice < 0:
  print("Invalid choice. You idiot.")
else:
  print(arr[user_choice])
  computer_choice = random.randint(0, 2)
  print("Computer chose:")
  print(arr[computer_choice])

  if user_choice > computer_choice:
    print("Yay You Win")
  elif user_choice == 0 and computer_choice == 1:
    print("Opps you loose")
  elif user_choice == 0 and computer_choice == 2:
    print("Yay you win")
  elif user_choice == 1 and computer_choice == 2:
    print("Opps you loose")
  else:
    print("Its a tie")