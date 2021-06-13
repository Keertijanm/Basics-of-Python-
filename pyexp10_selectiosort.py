""" KEERTI GUPTA ,                               1900320130082 - IT-B                    
                PYTHON -LAB_EXPERIMENT -10

Program -  To write a python selection sort 
"""
def selectionSort(array, size):
   
    for step in range(size):
        min_idx = step
        for i in range(step + 1, size):
            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i
         
        # put min at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])
        
print(" Enter list elements :")
data = list(input().split())
size = len(data)
selectionSort(data, size)
print('Sorted Array in Ascending Order:')
print(data)

