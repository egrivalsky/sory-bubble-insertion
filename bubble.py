def bubble_sort(arr):
    n = len(arr)-1
    for i in range(n):
        for j in range(0, n-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return(arr)
test_arr = [14, 2, 7, 27, 11, 23, 4, 90, 41, 1]
print(bubble_sort(test_arr))