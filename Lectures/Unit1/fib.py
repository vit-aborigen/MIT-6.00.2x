def fib(n, dict):
    if n in dict:
        return dict[n]
    dict[n] = fib(n-1, dict) + fib(n-2, dict)
    return dict[n]

dict = {0:1, 1:1}
print(fib(129, dict))