from multipledispatch import dispatch
import math

@dispatch(float)
def perimeter(radius):
    perimC = 2 * math.pi * radius
    print(f'Circle perimeter: {perimC}')

@dispatch(float, float)
def perimeter(length, width):
    perimR = 2 * (length + width)
    print(f'Rectangle perimeter: {perimR}')

@dispatch(float, float, float)
def perimeter(a, b, c):
    perimT = a + b + c
    print(f'Triangle perimeter: {perimT}')
    
perimeter(12.1)
perimeter(2.1, 3.0)
perimeter(3.0, 5.3, 7.1)

