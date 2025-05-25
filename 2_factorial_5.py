def facto(n):
    if n > 1:
        fact = facto(n-1) * n
        
    else:
     fact = 1
     
    return fact
    
print(facto(5))
