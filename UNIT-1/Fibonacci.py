
# FIBONACCI (NATIVE V/S MEMORIZED)

# NATIVE : CALCULATOR WITHOUT MEMORY (RECOUNTS EVERYTHING)
# MEMORIZED : CALCULATOR WITH MEMORY BUTTON (STORES ANSWERS)

naive_calls = 0
def fib_naive(n):
    global naive_calls
    naive_calls += 1
    if n <= 1:
        return n
    return fib_naive(n-1) + fib_naive(n-2)
print("fib_naive(4):", fib_naive(4))



#Memoized Fibonacci with call counter
memo_calls = 0
memo = {}
def fib_memo(n):
    global memo_calls
    memo_calls += 1
    if n in memo:
        return memo[n]
    if n <= 1:
        memo[n] = n
    else:
        memo[n] = fib_memo(n-1) + fib_memo(n-2)
    return memo[n]


# Compare call counts
for n in [5, 2, 3]:
    naive_calls = 0
    result_naive = fib_naive(n)
    print(f"fib_naive({n}) = {result_naive}, calls = {naive_calls}")

    memo_calls = 0
    memo = {}
    result_memo = fib_memo(n)
    print(f"fib_memo({n}) = {result_memo}, calls = {memo_calls}")
    print("---")