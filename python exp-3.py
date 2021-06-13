# KEERTI  GUPTA,    ROLL NO - 1900320130082   IT -B 

#  EXPERIMENT : 3  write a program to understand the GCD of two number in python

def gcd_fun (x, y):  
    if (y == 0): # it divide every number  
        return x  # return x  
    else:  
        return gcd_fun (y, x % y)  
x =int (input ("Enter the first number: ")) # take first no.   
y =int (input ("Enter the second number: ")) # take second no.   
num = gcd_fun(x, y) # call the gcd_fun() to find the result  
print("GCD of two number is: ")  
print(num)