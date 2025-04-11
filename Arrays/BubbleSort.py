# Bubble Sort

# time complexity: O(n^2)
# best case: O(n)

# space complexity: O(1), the input list is reused and modified in-place and the extra spaces only include a few integers

my_array = [7, 3, 9, 12, 11]

n = len(my_array)
for i in range(n - 1):  # an array with length of n needs to be looped at most n-1 times

    swapped = False  # the sub array has not been swapped

    # i elements have already been sorted
    # now it still needs n-i-1 comparisons to complete this loop
    for j in range(n - i - 1):
        if my_array[j] > my_array[j + 1]:
            my_array[j], my_array[j + 1] = my_array[j + 1], my_array[j]
            swapped = True
        print(my_array)  # print the result of each comparison

    # if there is no swap in this loop, it means the array has been completely sorted
    if not swapped:
        break

print("Sorted array: ", my_array)
