myArray = [170, 45, 75, 90, 802, 24, 2, 66]
print("Original array:", myArray)
radixArray = [[], [], [], [], [], [], [], [], [], []]
maxVal = max(myArray)
exp = 1

while maxVal // exp > 0:
    print("------------------------")

    while len(myArray) > 0:
        val = myArray.pop(0)
        radixIndex = (val // exp) % 10
        radixArray[radixIndex].append(val)
        print("exp=", exp)
        print("myArray: ", myArray)
        print("radixArray: ", radixArray)

    print("------------------------")

    for bucket in radixArray:
        while len(bucket) > 0:
            val = bucket.pop(0)
            myArray.append(val)
            print("myArray: ", myArray)
            print("radixArray: ", radixArray)

    exp *= 10

print("Sorted array:", myArray)
