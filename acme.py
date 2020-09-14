import random
class Product():
    def __init__(self, name, price = 10, weight = 20, flammability = 0.5, identifier = random.randint(100000, 9999999)):
        self.name = name
        self.price = price
        self. weight = weight
        self.flammabilty = flammability
        self.identifier = identifier

    def stealability(self):
        if self.price / self.weight < 0.5:
            print('Not so stealable...')
        elif self.price / self.weight < 1:
            print('Kinda stealable.')
        else:
            print('Very stealable!')

    def explode(self):
        if self.flammabilty * self.weight < 10:
            print(" ...fizzle")
        elif self.flammabilty * self.weight < 50:
            print(" ...boom!")
        else:
            print(" ...BABOOM!!")

class BoxingGlove(Product):
  def __init__(self, name, price = 10, weight = 10, flammability = 0.5, identifier = random.randint(100000, 9999999)):
      self.name = name
      self.price = price
      self.weight = weight
      self.flammabilty = flammability
      self.identifier = identifier

  def explode(self):
    print(" ...it's a glove.")

  def punch(self):
    if self.weight < 5:
        print("That tickles")
    elif self.weight < 15:
        print("Hey that hurt!")
    else:
        print("OUCH!")


