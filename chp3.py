# Arina Moroz
# November 9, 2023
# Player eats more than 5 candy, score doubles and 4th chapter unlocks. Otherwise they fail, and they go back to chapter 2.

import globalvariables


def chapterThree():  # Runs chapter Three
  print("You have successfully beaten the rain! Woho!")
  print("Oh no! I forgot to mention that monsters come out at night! ")
  print("Solve the equations before the monsters eat you up! ")
  while globalvariables.player.score > 0 and globalvariables.player.score < 50:
    askCandy()
    if globalvariables.player.score < 50:
      print("Not enough candies yet(need at least 50)! Go eat more candy!")
      globalvariables.printScore()
  if globalvariables.player.score <= 0:  # Score being 0 means that the user needs to go back to chapter 2 to gain more points.
    print("Disappointing, go back to the previous chapter and try harder!")
    globalvariables.player.score = 0
    globalvariables.chapter = 2
  else:
    print("Impressive! Move on to the next chapter!")
    globalvariables.chapter = 4


def askCandy():  # Asks 3 expressions and returns if the answer was correct
  candy = int(input("How many candies did you eat on Halloween? "))
  if candy >= 5:
    globalvariables.player.score *= 2
  elif candy > 0 and candy < 5:
    globalvariables.player.score -= 5
  else:
    print("Invalid number")


def main():
  globalvariables.gVariables()
  chapterThree()


if __name__ == "__main__":
  main()


