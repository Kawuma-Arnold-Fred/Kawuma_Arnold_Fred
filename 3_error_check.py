while True:
    try:
        a = float(input('Enter the first number'))
        b = float(input('Enter the second number'))
        
        c = a/b
        print(c)
        
        break
    
    except ValueError:
        print('The number entered is invalid')
        
    except ZeroDivisionError:
        print('You cannot divide by zero')
        
    except KeyboardInterrupt:
        print('\nProgram stopped by the user')
        
        break
    
        