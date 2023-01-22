#!/usr/bin/env python3
import random

choice = ["r","p","s"]

# (human, computer): win/lose/tie
win = {("r","r"): 'tie',
       ("p","p"): 'tie',
       ("s","s"): 'tie',
       ("r","s"): 'win',
       ("s","p"): 'win',
       ("p","r"): 'win',
       ("p","s"): 'lose',
       ("r","p"): 'lose',
       ("s","r"): 'lose'}

class Player:
  #points = 0
  def __init__(self, points = 0, move = ''):
    self.points = points
    self.move = move

  def setMove (self,move):
    self.move = move

  def getMove(self):
    return self.move

  def setPoint(self):
      self.points += 1

  def getPoints(self):
    return self.points


class HumanPlayer(Player):

  def setMove(self):
    move = input("\nRock, Paper or Scissors [r,p,s]? ")
    if (move in choice):
      self.move = move
    else:
       self.move = ""

class ComputerPlayer(Player):
  def setMove(self):
    self.move = random.choice("rps")



class Game:

  def __init__(self, repeat = 0):
    self.repeat = repeat
    self.hmn = HumanPlayer()
    self.comp = ComputerPlayer()

  def playGame(self,repeat):
    while repeat != 0:

      self.comp.setMove()
      self.hmn.setMove()
      while ( self.hmn.getMove() == ""):
        self.hmn.setMove()

      print( "You: " + self.hmn.getMove() + " | " + "Computer: " + self.comp.getMove())
      gamemoves = (self.hmn.getMove(), self.comp.getMove())

      if (gamemoves in win):
          if win.get(gamemoves) == "tie":
            print ("This round is a tie!")
          else:
            print ("You " + win.get(gamemoves)+ " this round!")
            if win.get(gamemoves) == 'win':
              self.hmn.setPoint()
            else:
              self.comp.setPoint()
      repeat -=1
    print("\n[ Game summary ]: Your points: " + str(self.hmn.getPoints()) + " | Computer points: " + str(self.comp.getPoints()))
    if self.hmn.getPoints() > self.comp.getPoints():
      print("You won.")
    elif self.hmn.getPoints() < self.comp.getPoints():
      print("Computer won.")
    else:
      print("It was a tie!")




def main():
  game = Game()
  play = True
  while play:
    numGames = input("""---  Rock Paper Scissors Game  --- \n
                      How many rounds do you want to play? """)

    if (numGames.isnumeric()):
      numGames = int(numGames)
      game.playGame(numGames)
      play = False



if __name__ == '__main__':
    main()
