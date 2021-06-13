"""
KEERTI GPTA IT-B 190032130082
         PYTHON LAB - EXP NO- 12
PROGRAM- write a python program to print first n prime numbers  
"""
print("value of n")
num = int(input())
t=0
print("first nth prime numbers are")
for j in range(2,num*(num-2)):
    for i in range(2,j):
        if j%i == 0:
            break
    else:
        if(t<num):
            print(j)
            t =t+1

print("counting of  prime number which  are print: ")
print(t)
