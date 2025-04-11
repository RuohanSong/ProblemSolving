print(0)
print(1)
count = 2

def fibonacci(prev1, prev2):
    global count
    if count <= 15:
        new_fibo = prev1 + prev2
        print(new_fibo)
        prev1 = prev2
        prev2 = new_fibo
        count += 1
        fibonacci(prev1, prev2)
    else:
        return

fibonacci(0, 1)