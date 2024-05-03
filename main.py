# Arina Moroz
# November 9, 2023
# Managing chapters

import globalvariables
import startgame
from chp1 import chapterOne
from chp2 import chapterTwo
from chp3 import chapterThree
from chp4 import chapterFour
from chp5 import chapterFive
import time


def main():
  globalvariables.gVariables()  # initiallizes the global variables
  while (globalvariables.chapter !=
         999):  #the game will run until globalvariables.chapter is set to 999
    if (globalvariables.chapter == 0):
      startgame.startGame()
    if (globalvariables.chapter == 1):
      globalvariables.printHeader()
      time.sleep(1)
      chapterOne()
    elif globalvariables.chapter == 2:
      globalvariables.printHeader()
      time.sleep(1)
      chapterTwo()
    elif globalvariables.chapter == 3:
      globalvariables.printHeader()
      time.sleep(1)
      chapterThree()
    elif globalvariables.chapter == 4:
      globalvariables.printHeader()
      time.sleep(1)
      chapterFour()
    elif globalvariables.chapter == 5:
      globalvariables.printHeader()
      time.sleep(1)
      chapterFive()

  print("Game complete!")


if __name__ == "__main__":
  main()
