arr = [4, 2, [6, 3], [1, [9, 8]], 5]

largestval = float('-inf')

def greatetval(arr):
    largestval = float('-inf')
    for item in arr:
        if isinstance(item, int):
            largestval = max(item, largestval)

        if isinstance(item, list):
            largestval = max(largestval, greatetval(item))

    return largestval

print(greatetval([4, 2, [6, 3], [1, [9, 8, 17, [4, 6, 23]]], 5]))

