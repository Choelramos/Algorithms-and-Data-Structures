"""Dado um array que pode conter matrizes aninhadas,
profuz um simples array resultante
Não entendi muito bem a implementação, voltarei a estudar"""

from collections.abc import Iterable


def flatten(input_arr, output_arr=None):
    if output_arr is None:
        output_arr = []
    for ele in input_arr:
        if not isinstance(ele, str) and isinstance(ele, Iterable):
            flatten(ele, output_arr)  # Recursão
        else:
            output_arr.append(ele)
    return output_arr
