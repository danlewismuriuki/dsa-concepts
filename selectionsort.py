my_array = [54, 56, 56, 89, 98, 34, 67]

n = len(my_array) #get length of the array
for i in range(n): # lop through the array
    for j in range(i+1, n): # start from the current i+1 loop onwards
        if my_array[j] < my_array[i]: # if the next val is less than prev
            my_array[j], my_array[i] = my_array[i], my_array[j] # swap

print("sorted:", my_array)