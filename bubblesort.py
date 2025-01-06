my_array = [54, 56, 56, 89, 98, 34, 67]

n = len(my_array)

for i in range(n):
    for j in range(n-i-1): # reduce the current number of index we are on as there are a similar number at the end which ahs beeen sortedlast index
        if my_array[j] > my_array[j+1]: # if the array at the curent second loop to loop through the swaps is greater than than the next one 
            my_array[j], my_array[j+1] = my_array[j+1], my_array[j]  # swap the two

print("bubblesort:", my_array)