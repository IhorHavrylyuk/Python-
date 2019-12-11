class Buyer:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name

class Alcohol:
    def __init__(self, name, buyer):
        self.name = name
        self.buyer = buyer

    def buy(self):
        if self.buyer.age >= 21:
            print("{} bought {}".format(self.buyer.getName(), self.name))
        else:
            print('This buyer is too young!!!')

if __name__ == '__main__':
    person1 = Buyer('Andriy', 21)
    person2 = Buyer('Bohdan', 19)
    alcohol = Alcohol('wine', person1)
    alcohol.buy()
    alcohol = Alcohol('wine', person2)
    alcohol.buy()