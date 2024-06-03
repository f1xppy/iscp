import time
import random


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + mid + quicksort(right)
'''
в среднем имеет временную сложность O(n*log(n))
'''


arr = [i + random.randint(1,10000) for i in range(0, 1000000)]
start_time = time.time()
qs = quicksort(arr)
end_time = time.time()
print(end_time-start_time)

start_time = time.time()
s = sorted(arr)
end_time = time.time()
print(end_time-start_time)

'''
по результатам тестов встроенная в python функция для сортировки является наиболее оптимальной
использует гибридный метод сортировки (вставками или слиянием)
'''
