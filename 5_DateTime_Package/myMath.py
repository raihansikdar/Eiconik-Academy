from functools import reduce

def add(x: int, y: int) -> int:
    return x+y
def sub(x: int, y: int) -> int:
    return x-y

class Math_Class:
    def __init__ (self, nums: list([int])) -> None:
        self.nums = nums
    
    def sum(self) ->int:
        add = lambda x,y: x+y
        return reduce(add,self.nums)

var = 9


if __name__ == "__main__":
    print("This is math file!")