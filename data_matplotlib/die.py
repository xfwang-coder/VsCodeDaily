from random import randint

class Die():
    """定义一个骰子的类"""
    def __init__(self,num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        """投掷一次骰子，即返回一个点数"""
        return randint(1,self.num_sides)
