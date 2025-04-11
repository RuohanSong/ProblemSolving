# time complexity: O(nlog(n))
# worst case: O(n^2)

# space complexity: O(log(n))

def partition(array, low, high):
    pivot = array[high]     # choose the last element as the pivot
    i = low - 1     # i tracks the position of the "smaller" elements
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i+1], array[high] = array[high], array[i+1]

    print("i=", i, "--", array)
    return i+1


def quicksort(array, low=0, high=None):
    if high is None:
        high = len(array) - 1

    if low < high:
        pivot_index = partition(array, low, high)
        print("pivot index = ", pivot_index)
        quicksort(array, low, pivot_index-1)
        quicksort(array, pivot_index+1, high)


my_array = [64, 34, 25, 12, 22, 11, 90, 5]
quicksort(my_array)
print("Sorted array:", my_array)