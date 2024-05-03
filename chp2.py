# Arina Moroz
# November 9, 2023
# Player gets to decide if they still want to keep playing, if yes, the game goes on to solving experssions, and if the player gets 2 or more problems correct, they move on the the 3rd chapter.

import globalvariables


def chapterTwo():  # Runs chapter Two
  print("Phew! That was a really close one out there! Nice job! ")
  print("But that doesn't seem to be all! I see another attack happening!")
  print(
      "This one seems like it's raining big heavy ornaments, and it's getting darker and darker every minute"
  )
  print(
      "You must complete these expressions before its too late! I'm going to go and hide for now. Good luck! "
  )
  solved = False
  correct = 0
  while (not solved):
    answer = input("Do you want to solve an expression? [Y/N] ")
    if answer.lower() == 'n':
      print("Too bad!")
      globalvariables.chapter = 999
      return
    elif answer.lower() == 'y':
      print("Great let's go!")
      solved, correct = solveExpressions()
    else:
      print("Weird way to say yes, but ok!")
      solved, correct = solveExpressions()
    if (solved):
      globalvariables.player.score += correct * 10
      globalvariables.chapter = 3


def solveExpressions(
):  # Asks 3 expressions and returns if the answer was correct
  correct = 0
  questions = [[2, 3], [13, 4], [54, 37]]
  for a, b in questions:
    answer = input(f"What is {a} x {b}? ")
    if answer == str(a * b):
      print("Correct!")
      correct += 1
    else:
      print("Incorrect!")
  print(f"You got {correct} of 3 questions right")
  if correct >= 2:
    print("Move on to the next chapter!" )  # Player wins, they move to the next level
    print("Yay!!! We have been rescued, and it seems like the sky is slighlty starting to clear up again. " )
    return True, correct
  else:
    print("Not enough to move on, go back and try again")
    return False, correct


def main():
  globalvariables.gVariables()
  chapterTwo()


if __name__ == "__main__":
  main()
