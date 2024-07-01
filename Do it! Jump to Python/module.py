# Module
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

# Import
from mod1 import add, sub
from mod1 import *

# if__name__=="__main__":
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

if __name__ == "__main__":
    print(add(1, 4))
    print(sub(4, 2))

# Class & Variable
PI = 3.141592

class Math:
    def solv(self, r):
        return PI * r * r
    
def add(a, b):
    return a + b

# sys.path.append
sys.path
sys.path.append("C:/Users/Python")

# PYTHONPATH
set PYTHONPATH = C:/Users/Python
import mod2
print(mod2.add(3, 4))

