""" KEERTI GUPTA ,                               1900320130082 - IT-B                    
                PYTHON -LAB_EXPERIMENT -8

Program -  To write a python program  of liner search 

"""

def linear_Search(list1, n, key):  
  
    # Searching list1 sequentially  
    for i in range(0, n):  
        if (list1[i] == key):  
            return i  
    return -1  
  
print(" Enter list elements :")
list1 = list(map(int, input().split()))
key = int(input("Enter the key or searching element: "))  
  
n = len(list1)  
res = linear_Search(list1, n, key)  
if(res == -1):  
    print("Element not found")  
else:  
    print("Element found at index: ", res)  