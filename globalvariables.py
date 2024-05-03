# Arina Moroz
# November 9, 2023
# All of my variables written here

class Character:

    def __init__(self, name, score):
      self.name = name
      self.score = score

def gVariables():
    global player
    global chapter

player = Character("Tom", 0)  # Default player name and starting score
chapter = 0

def printHeader():
    print(f"Welcome {player.name} to chapter {chapter}")
    printScore()

def printScore():
    print(f"{player.name} score is {player.score}")

if __name__ == "__main__":
    gVariables()


