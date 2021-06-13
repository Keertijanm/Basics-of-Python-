""" KEERTI GUPTA ,                               1900320130082 - IT-B                    
                PYTHON -LAB_EXPERIMENT -7

Program -  To write a python program find maximum of a list of numbers 

"""
print(" Enter list elements :")
lst = list(map(int, input().split()))

lst.sort()
print("maximum  number in  a list of numbers is:", lst[-1])