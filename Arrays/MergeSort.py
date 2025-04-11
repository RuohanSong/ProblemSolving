def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    leftHalf = arr[:mid]
    rightHalf = arr[mid:]

    print("left: ", leftHalf)
    print("right: ", rightHalf)
    print("-------------------")

    sortedLeft = mergeSort(leftHalf)
    sortedRight = mergeSort(rightHalf)

    print("sorted left: ", sortedLeft)
    print("sorted right: ", sortedRight)
    print("-------------------")

    return merge(sortedLeft, sortedRight)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
            print("result: ", result)

        else:
            result.append(right[j])
            j += 1
            print("result: ", result)

    result.extend(left[i:])
    result.extend(right[j:])

    print("result: ", result)
    print("-------------------")

    return result


unsortedArr = [3, 7, 6, -10, 15, 23.5, 55, -13]
sortedArr = mergeSort(unsortedArr)
print("Sorted array:", sortedArr)

#Python