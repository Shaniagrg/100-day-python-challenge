from typing import TypeVar
T = TypeVar('T') 

def input(prompt:T, input_type: T)->T:
    return input_type

age:int = input("What is your age? ")

name:str = input("What is your name? ")
print(age)


