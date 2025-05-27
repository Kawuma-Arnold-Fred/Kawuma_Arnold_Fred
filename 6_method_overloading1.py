from multipledispatch import dispatch
import math

@dispatch(float, float)
def area(length, width):
    areaQ = length * width
    print(f'Rectangle/Circle area: {areaQ}.')
    
@dispatch(float)
def area(radius):
    areaC = math.pi * (radius * radius)
    print(f'Cricle area: {areaC}') 
    
area(2.5,9.0)
area(3.2)
 