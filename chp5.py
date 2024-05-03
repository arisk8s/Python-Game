# Arina Moroz
# Novemeber 10, 2023
# Calculating the players total and if they win, they get 5 stars, if not than they need to go to different chapters.
import globalvariables
import time


def chapterFive():  # Runs chapter Five
  if globalvariables.player.score > 120:  # more than 100 points, winner gets a prize.
    print("Congragulations! You have made it! ")
    print(
        "The monsters have been beated, and look, the sky is completely clear now! "
    )
    print(f"Well Done {globalvariables.player.name}! You get 5 stars")
    globalvariables.chapter = 999
  elif globalvariables.player.score > 70 and globalvariables.player.score <= 120:
    print(f"Good try {globalvariables.player.name}! But you did not earn enough points to beat the monsters! You need to go back and score more points to defeat them!")
    print("Let's go back to chapter 4 and try to score more points")
    globalvariables.chapter = 4
    time.sleep(1)
  else:  # Player doesn't have enough points to win, goes back to chapter 3.
    print(f"You need to try harder {globalvariables.player.name}! The monsters won't be beat by this low score, you need to gather more points to be able to defeat them.")
    print("Go back to chapter 3 and score more points")
    globalvariables.chapter = 3
    time.sleep(1)


def main():
  globalvariables.gVariables()
  chapterFive()


if __name__ == "__main__":
  main()

