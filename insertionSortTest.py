

#Make an array for the sorting of a selection

array = [13,4,9,5,3,16,12]

def selectionSort (array):#passing the array in the function header

    n = len(array)

    for i in range(n):#whatever the length of the array, is how many times you are going to run the loop

        #initally assume the first element of the unsorted part as the minimum
        minimum = i

        for j in range(i+1, n):
            if (array[j] < array[minimum]):
                minimum = j
        #swaping the minimum element with the first element of the unsorted part of the array   
        temp = array[i]
        array[i] = array[minimum]
        array[minimum] = temp

    return array

print(selectionSOrt(array))