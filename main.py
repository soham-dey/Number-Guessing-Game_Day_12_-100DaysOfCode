from art import logo
from replit import clear
import random

def game():
  """Calls the number guessing game."""
  print(logo)

  print("\nWelcome to the Number Guessing Game!\nI am thinking of a number between 1 and 100.\n")
  #prompt to user for choosing difficulty level
  difficulty_level=input("Choose your difficulty level- hard, medium or easy: ")
  difficulty_dict={"hard":5, "medium":10, "easy":15}
  #creates a list containing numbers from 1 to 100
  num_list=[]
  for i in range(1,101):
    num_list.append(i)

  #computer chooses a random integer from the range of (1,100)
  computer_choice=random.choice(num_list)
  correct="No"

  #Based on the difficulty level, the number of attempts is chosen and the computer checks when the #user makes a right guess, simultaneously keeping a count of the number of attempts left.
  guessed_no_list=[]
  for key in difficulty_dict:
    if difficulty_level==key:
      number_of_attempts=difficulty_dict[key]
      while number_of_attempts>=1 and correct=="No":
        print(f"You have {number_of_attempts} of attempts left.")
        guess=int(input("Guess your number: "))
        if guess==computer_choice:
          correct="Yes"
          print("You have guessed right!")
        elif guess<computer_choice:
          correct="No"
          print("Too low!")
          number_of_attempts-=1
        elif guess>computer_choice:
          correct="No"
          print("Too high!")
          number_of_attempts-=1
      if number_of_attempts==0 and correct=="No":
        print("You have lost! Game Over")

  #propmts the user to choose if s/he wants to start a new game or not
  yes_or_no=input("Do you want to start a new game? Type 'yes' or 'no': ")
  if yes_or_no=="yes":
    clear()
    game()
  else:
    clear()

#calls the game function
game()






