"""
Dado uma lista lst e um número N, criar uma lista
que contém cada número da lista no máximo N vezes, sem reordenar.

Por exemplo: if N = 2, e a entrada é [1,2,3,1,2,1,2,3], você terá [1,2,3,1,2],
retira o próximo  [1,2], visto que isso levaria 1 e 2 ao resultado 3 vezes, e então pega 3
que leva ao resultado [1,2,3,1,2,3]
O método nativo tem complexidade O(n^2)
Já o método usando hash tables é O(n)
"""
import collections


def delete_nte_native(array, n):
    ans = []
    for num in array:
        if ans.count(num) < n:
            ans.append(num)
    return ans


def delete_nth(array, n):
    result = []
    counts = collections.defaultdict(int)

    for i in array:
        if counts[i] < n:
            result.append(i)
            counts[i] += 1
    return result


arr = [1, 2, 1, 3, 1, 4, 1, 5, 5, 5]
operacao = delete_nth(arr, 2)
print(operacao)
