# Run Length Encoder

# Implement a simple Run Length Encoder, shortening sequences of the same characters.
# Sample input: aaabbccca
# Sample output: a3b2c3a1

def RunLengthEncoder(input):
    if not input:   # handle empty string
        return ""

    output = [input[0]]
    currentcount = 1

    for i in range(1, len(input)):
        if input[i] != input[i-1]:
            output.append(str(currentcount))
            output.append(input[i])
            currentcount = 1
        else:
            currentcount += 1

    output.append(str(currentcount))    # Final count for the last character
    output_string = ''.join(output)

    return output_string


input = "aaabbcccaaa"
print(RunLengthEncoder(input))