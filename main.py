import random as ran
from characters import MainCharacter, Trader, Character



#  Controls the game state
class GameState:

  def __init__(self):
    self.__mainChar = MainCharacter()
    self.__aliveChars = [Trader]

    # Main Gameplay Loop
    while self.getIsMainCharAlive(self.getAliveChars()):
      currChar = self.getRandomAliveChar(self.getAliveChars())

  def getAliveChars(self):
    return self.__aliveChars

  def getMainChar(self):
    return self.__mainChar
      

  def getIsMainCharAlive(self, aliveChars):
    for i in range(len(aliveChars)):
      if self.getAliveChars()[i].getName() == self.getMainChar().getName():
        return True

    return False

  def getRandomAliveChar(self, aliveChars):
    ranNum = ran.randint(0, len(aliveChars) - 1)
    return aliveChars[ranNum]


gameState = GameState()
