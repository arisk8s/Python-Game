# Arina Moroz
# Novemeber 10, 2023
# Player gets two options on how to solve a problem in order to go on to the 2nd chapter.

import globalvariables

print("It was a dark stormy night, where all the holidays were doomed!")
print("The only way to clear out the storm that is happening and save the holidays is by going through some challenges! ")
print("As each challenge gets harder and harder, the more you answer, the more the sky starts to clear up with children coming out happy. ")
print("To start off, let's play the game! ")


def chapterOne():  # Runs chapter One
  solved = False
  while (not solved):
    print("Hurry! The lightning's and thunder are about to attack everyone! ")
    choose = input("Choose a game: [1] Math Equation [2] Solve a riddle ")
    if (choose == '1'):
      solved = askMath()
    elif (choose == '2'):
      solved = askRiddle()
    else:
      print("Invalid choice, try again!")
  globalvariables.player.score = 5
  globalvariables.chapter = 2


def askMath():  # Asks a math question and returns if the answer was correct
  print("Hurry! The lightning's and thunder are about to attack everyone! ")
  answer = input("What is 64 divided by 2? ")
  if (answer == "32"):
    print("That's right!")
    return True
  else:
    print("Oh no, wrong answer!")
    return False


def askRiddle():  # Asks a riddle and returns if the answer is correct
  answer = input("What is yours but mostly used by others? ")
  if (answer.lower() == "name"):

    print("That's right!")
    return True
  else:
    print("Oh no, wrong answer!")
    return False


def main():
  globalvariables.gVariables()
  chapterOne()


if __name__ == "__main__":
  main()


