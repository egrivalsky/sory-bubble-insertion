# quick sort is a logarithmic algorithm

import random, time

sample1 = random.sample(range(1, 1000000), 100)
sample2 = random.sample(range(1, 1000000), 9999)
#sample3 = random.sample(range(1, 1000000), 200000)

quick_computation = 0
bubble_comp = 0
# this is a recursive quick sort algo
def quick_sort(array):
    global quick_computation
    quick_computation += 1

# 3 lists, 1 pivot
# base case: consider length of list. If it's <= 1, return it

    left_list = []
    mid_list = []
    right_list = []

    if len(array) <= 1:
        return array

    pivot = array[0] # our pivot is the first element in the list

    for num in array:
        if num < pivot:
            left_list.append(num)

        elif num == pivot:
            mid_list.append(num)

        elif num > pivot:
            right_list.append(num)

    return quick_sort(left_list) + mid_list + quick_sort(right_list)

def bubble_sort(arr):
    global bubble_comp
    n = len(arr)
    for i in range(n):
    # this is the number of loops we do
        for j in range(0, n-i-1):
            bubble_comp += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print(bubble_comp)
    return arr

# comparing the time it takes to sort a given list (bubble sort v quick sort)
quick_start_time = time.time()
print(quick_sort(sample3))
quick_end_time = time.time()

bubble_start_time = time.time()
print(bubble_sort(sample3))
bubble_end_time = time.time()

print('Quick Sort Time:', quick_end_time - quick_start_time)
print('Quick Sort Computations', quick_computation)

print('Bubble Sort Time: ', bubble_end_time - bubble_start_time)
print('Bubble Sort Computations: ', bubble_comp)

