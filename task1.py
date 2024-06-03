def is_even(value):
    return (value & 1) == 0

s = int(input())
print(is_even(s))

'''
Оператор & (побитовое И)
"И" между числом и 1 возвращает 0 в случае, когда последний бит числа равен 0 => является четным 
Побитовые операции выполняются быстрее чем деление (т.к. выполняются на более низком уровне)
'''