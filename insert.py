def insertion_sort(arr):
    operations = 0
    for i in range(len(arr)):
        num_we_are_on = arr[i]
        j = i - 1
                # do a check to make sure j doesn't go over the edge
        while j >= 0 and arr[j] > num_we_are_on:
            operations += 1
            arr[j+1] = arr[j]
            j -= 1
        j += 1
        arr[j] = num_we_are_on

    return arr, operations

test_arr = [3, 4, 5, 8, 34, 9, 45, 89, 3, 12]
#tuple unpacking: return two values at once
ordered_array, operations = insertion_sort(test_arr)
print(ordered_array, operations)