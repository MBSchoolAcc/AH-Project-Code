import random as ran
import globalFiles as gF


#  Character Classes
class Character:

  def __init__(self, name, health, strength):
    self.__name = name
    self.__health = health
    self.__strength = strength

  def getName(self):
    return self.__name

  def setName(self, name):
    self.__name = name

  def getHealth(self):
    return self.__health

  def setHealth(self, health):
    self.__health = health

  def getStrength(self):
    return self.__strength

  def setStrength(self, strength):
    self.__strength = strength

  def die(self, aliveChars):
    aliveChars.remove(self)
    del self
    
  def leave(self):
    del self
    


class MainCharacter(Character):

  def __init__(self):
    super().__init__("You", 100, 5)
    self.__items = self.getRandomStartItems()
    self.__sanity = 0


  def getSanity(self):
    return self.__sanity

  def setSanity(self, sanity):
    self.__sanity = sanity

  def getItems(self):
    return self.__items

  def removeItem(self, item):
    self.__items.remove(item)

  def addItem(self, item):
    self.__items.append(item)

  def getRandomStartItems(self):
    randomItems = []
    allItems = []
    if len(allItems) < 1:
      return randomItems

    ranNum = ran.randint((len(allItems) - 2), len(allItems))


    for i in range(ranNum):
      ranNum2 = ran.randint(0, len(allItems) - 1)
      randomItems.append(allItems[ranNum2])
      allItems.pop(ranNum2)

    return randomItems

  def shoot(self, target, aliveChars):
    target.die(aliveChars)


class Trader(Character):
  def __init__(self, mainCharacter):
    super().__init__("Trader", 75, 2)

    self.trade1 = Trade()
    self.trade2 = Trade()
    self.trade3 = Trade()

    self.encounter(mainCharacter)

  def getTrade1(self):
    return self.trade1

  def getTrade2(self):
    return self.trade1

  def getTrade3(self):
    return self.trade1

  def encounter(self, mainCharacter):
    print("A strange man approaches your bunker wearing a cloak and fedora, he knocks on the door and yells 'We do deal. I give.'")
    print("\n1 - Open door\n2 - Ignore")
    
    choice = gF.getChoice(2)
    if choice == 2:
      self.leave()

    elif choice == 1:
      print("'I give this you give that?'")
      print("\n1 -", self.getTrade1().getItem1().getName(), "for", self.getTrade1().getItem2().getName())
      print("\n2 -", self.getTrade2().getItem1().getName(), "for", self.getTrade2().getItem2().getName())
      print("\n3 -", self.getTrade3().getItem1().getName(), "for", self.getTrade3().getItem2().getName())
      choice == gF.getChoice(3)
      
    
    if choice == 1:
      self.getTrade1().completeTrade(self, mainCharacter)
      
    elif choice == 2:
      self.getTrade2().completeTrade(self, mainCharacter)
      
    elif choice == 3:
      self.getTrade3().completeTrade(self, mainCharacter)

    print("The man quickly scurries away and soon disappears into the distance.")


class Trade():
  def __init__(self):
    self.__item1 = gF.getRandomItem()
    self.__item2 = gF.getRandomItem()
    while self.getItem2 == self.getItem1:
      self.__item2 = gF.getRandomItem()

  def getItem1(self):
    return self.__item1

  def setItem1(self, item1):
    self.__item1 = item1

  def getItem2(self):
    return self.__item2

  def setItem2(self, item2):
    self.__item2 = item2

  def completeTrade(self, trader, mainCharacter):
    print("Yes good deal...")
    mainCharacter.removeItem(self.getItem1())
    mainCharacter.addItem(self.getItem2())
    trader.leave()
  
