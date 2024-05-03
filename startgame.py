# Arina Moroz
# November 9, 2023
# Asks the player for there name before starting the game.

import globalvariables
import time

def startGame():
  globalvariables.player.name = input("What is your name? ")

  begin_answer = input("Would you like to begin playing? Yes/No ")
  begin_play = 0
  if begin_answer == "No" or begin_answer == "no":
    print("Why did you start this up, then?")
    begin_play = 0
    time.sleep(1)
    exit()  # Quits the game and closes the client.

  elif begin_answer == "Yes":
    print("Alright, let's begin!")
    time.sleep(1)
    begin_play = 1

  else:
    print("Weird way to spell 'Yes', but that's alright!")
    time.sleep(1)
    begin_play = 1

  globalvariables.chapter = begin_play


if __name__ == "__main__":
  startGame()