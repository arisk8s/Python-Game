# Arina Moroz
# Novemeber 10, 2023
# Player needs to keep trying till they open all the boxes.
import globalvariables


def chapterFour():  # Runs chapter Four
  print("The monsters are about to eat you! ")
  print(
      "You need to solve the 3 equations in order to not become meat to them!")
  print("If you get two wrong, you will be eaten by the monsters!")
  boxes = ["red", "blue", "green"]
  while len(boxes) > 0:
    print(f"There are {len(boxes)} box(es) in front of you.")
    for b in boxes:
      print('[' + b + ']')
    box = input("Which one do you want to open? ")
    if box.lower() in boxes:
      solved = solveBox(box)
      if (solved):
        print(f"Congratulations, you opened {box.lower()} box!")
        globalvariables.player.score += 20
        globalvariables.printScore()
        boxes.remove(box.lower())
      else:
        print("Uh-oh! The box did not open. Try again!")
        globalvariables.player.score -= 5
        globalvariables.printScore()
    else:
      print("That's not a valid choice, try again!")
  globalvariables.chapter = 5


def solveBox(
    box
):  # Asks player to open 3 boxes and solve the expressions. Returns if the answer was correct
  if box.lower() == "red":
    answer = input("Solve for x: 3x = 24? ")
    return answer == "8"
  elif box.lower() == "blue":
    answer = input("Solve for a: 5+a = 7? ")
    return answer == "2"  # each box with an expression
  elif box.lower() == "green":
    answer = input("Solve for y: 8 = 2(y+2)? ")
    return answer == "2"
  else:
    return False


def main():
  globalvariables.gVariables()
  chapterFour()


if __name__ == "__main__":
  main()
