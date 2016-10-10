import random


class Dice:
    numbers = list(range(1,7))
    def roll(self):
        return random.choice(self.numbers)
    
class Sums:
    sum_list = list(range(3,19))
    def sum(self):
        return random.choice(self.sum_list)
    
    
    
if __name__ == "__main__":
    print(Dice().roll())
    print(Sums().sum())