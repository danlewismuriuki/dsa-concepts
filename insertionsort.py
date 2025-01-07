my_array = [54, 56, 56, 89, 98, 34, 67]

def insertion_sort(my_array):
    for i in range(1, len(my_array)):
        j = i
        while(j > 0 and my_array[j] < my_array[j - 1]):
            my_array[j], my_array[j - 1] = my_array[j - 1], my_array[j]
            j -= 1

insertion_sort(my_array)        
print("sorted", my_array)