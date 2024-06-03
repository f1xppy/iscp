from collections import deque


class ListBuffer:
    def __init__(self, size):
        self.buffer = [None] * size
        self.max_size = size
        self.head = 0
        self.tail = 0
        self.full = False

    def is_full(self):
        return self.full

    def is_empty(self):
        return not self.full and self.head == self.tail
    
    def enqueue(self, item):
        if self.full:
            raise IndexError("Buffer is full")
        self.buffer[self.tail] = item
        self.tail = (self.tail + 1) % self.max_size
        if self.tail == self.head:
            self.full = True

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Buffer is empty")
        item = self.buffer[self.head]
        self.buffer[self.head] = None
        self.head = (self.head + 1) % self.max_size
        self.full = False
        return item
    
'''
Буфер на основе списка - прост в реализации, позволяет полностью контролировать состояние буфера, 
но операции добавления/удаления (enqueue и dequeue) не оптимальны
'''    


class DequeBuffer:
    def __init__(self, size):
        self.buffer = deque(maxlen=size)

    def is_full(self):
        return len(self.buffer) == self.buffer.maxlen

    def is_empty(self):
        return len(self.buffer) == 0
    
    def enqueue(self, item):
        if self.is_full():
            raise IndexError("Buffer is full")
        self.buffer.append(item)
        
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Buffer is empty")
        return self.buffer.popleft()
    
'''
Управление буфером и отслеживание состояния производится автоматически, 
высокая производительность для операций добавления/удаления,
но может потреблять большее кол-во памяти, чем буфер на основе списка
'''

buffer = DequeBuffer(2)
buffer.enqueue(1)
buffer.enqueue(2)
print(f"{buffer.dequeue()}, {buffer.dequeue()}")