def mergesort(arr):
    length = len(arr)
    
    if length <= 1:
        return arr

    mid = length // 2    
    leftarr = arr[:mid]
    rightarr = arr[mid:]

    sortedLeft = mergesort(leftarr)
    sortedRight = mergesort(rightarr)

    return merge(sortedLeft, sortedRight)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

unsortedArr = [3, 7, 6, -10, 15, 23.5, 55, -13]
sortedArr = mergesort(unsortedArr)
print("Sorted array:", sortedArr)