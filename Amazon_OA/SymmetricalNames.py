import os
from collections import Counter


def getEncodedName(letters):
    freq = Counter(letters)
    firsthalf = []
    midchar = ""

    # go through all the characters in alphabetic order
    for char in sorted(freq.keys()):
        count = freq[char]
        # a symmetrical string only has at most one character with odd count
        # which could be midchar
        # exp: "abcba"
        # "yxxy" does not have a midchar
        if count % 2 == 1:
            # if midchar already exists but we found another odd count
            # this string is invalid
            if midchar:
                return ""
            # if midchar does not exists
            # this character is midchar
            midchar = char
        # one character presents count/2 times in the first half
        firsthalf.append(char * (count // 2))

    # build string using the list firsthalf
    firsthalf_str = "".join(firsthalf)
    return firsthalf_str + midchar + firsthalf_str[::-1]


letters = input()
result = getEncodedName(letters)
print(result)