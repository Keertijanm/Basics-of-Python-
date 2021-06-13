#  KEERTI GUPTA ,       IT-B                ROLL NO - 1900320130082

#write a python program to find the square root of a number (newton’s method)
def squareRoot(n, l) :
  
    # Assuming the sqrt of n as n only 
    x = n 
  
    # To count the number of iterations 
    count = 0 
  
    while (1) :
        count += 1 
  
        # Calculate more closed x 
        root = 0.5 * (x + (n / x)) 
  
        # Check for closeness 
        if (abs(root - x) < l) :
            break 
  
        # Update root 
        x = root
  
    return root 
  
# Driver code 
if __name__ == "__main__" : 
  
    n = 327
    l = 0.00001 
    print("square root of no is :")
  
    print(squareRoot(n, l)) 