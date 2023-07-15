# Essa primeira implementação de do algorítimo é muito lenta, complexidade O(2^n)
def fib_recursive(n):
    assert n >= 0
    if n <= 1:
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)


# print(fib_recursive(35))

# Já essa é bem mais rápida O(n)


def fib_iter(n):
    assert n >= 0
    fib_1 = 0
    fib_2 = 1
    res = 0
    if n <= 1:
        return n
    for _ in range(n-1):
        res = fib_1 + fib_2
        fib_1 = fib_2
        fib_2 = res
    return res


# print(fib_iter(100))

# Este exemplo também é rápido, complexidade O(n)
# Esse método usa programação dinâmica

def fib_list(n):
    assert n >= 0
    list_results = [0, 1]
    for i in range(2, n+1):
        list_results.append(list_results[i-1] + list_results[i-2])
    return list_results


print(fib_list(100))
