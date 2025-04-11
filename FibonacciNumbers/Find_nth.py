# Iterative with time complexity O(n) and space complexity O(1)
def F(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b


# Memoized Recursion with time complexity O(n) and space complexity O(n)
# def F(n, memo={}):
#     if n in memo:
#         return memo[n]
#     if n <= 1:
#         return n
#     memo[n] = F(n - 1, memo) + F(n - 2, memo)
#     return memo[n]


# Naive Recursion with time complexity O(2^n) and space complexity O(n)
# def F(n):
#     if n <= 1:
#         return n
#     else:
#         return F(n - 1) + F(n - 2)

print(F(100))
