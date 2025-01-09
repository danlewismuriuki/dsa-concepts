def quick_sort(sequence):
    if len(sequence) <= 1: # check the length of the array
        return sequence # return the array if len is 1 example [3]
    else:
        pivot = sequence.pop()  # else pop the last item in the array 

    items_greater = []  # create arrays to hold 
    items_lesser = []

    for item in sequence:  # if item is greater append it ti the greater array
        if item > pivot:
            items_greater.append(item)
        else:
            items_lesser.append(item)  # else append to the less array
    return quick_sort(items_lesser) + [pivot] + quick_sort(items_greater)  # recursively repeat the process again



print(quick_sort([54, 56, 56, 89, 98, 34, 67]))
