

def bubble_sort (array) :
    
    length = len(array)

    for i in range(length):
        a = length-i-1 #in order to check the last index, otherwise we would be out of bounds
        for j in range(a):
            #print("j in the range from 0 to length-i-1",j)
           if array[j] > array[j+1]:
               array[j], array[j+1] = array[j+1], array[j]
                
    return array