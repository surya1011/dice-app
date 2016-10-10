from dice import Dice
from dice import Sums

class Start:
    def __init__(self):
        self.sum = Sums().sum()
        print("""match the number {} by rolling the die for three times
roll : Y/N
              """.format(self.sum))
        self.choice = input().strip().lower()
        if self.choice == 'y':
            self.start()
        else:
            Start()
            
    def start(self):
        self.roll_list = []
        for i in range(3):
            print('Rolling...')
            self.roll_list.append(Dice().roll())
            print('roll {}: {} '.format(i,self.roll_list[i]))
        self.end()
        
    def end(self):
        if self.sum == len(self.roll_list):
            print("Congrats!!! You Won the Challenge")
        else:
            print("Bummer!! You lost the game")    
        key = input("press any key to continue")
        if key:
            Start()
            
if __name__ == "__main__":
    Start()
        