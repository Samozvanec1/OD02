class Queue:
    def __init__(self):
        self.items = [] # создаем пустую очередь

    def isEmpty(self):
        return self.items == [] # проверка на пустоту

    def enqueue(self, item):
        self.items.insert(0, item) # вставляем в начало

    def peek(self):
        return self.items[-1] # возвращаем с конца

    def dequeue(self):
        return self.items.pop() # удаляем с конца

    def size(self):
        return len(self.items) # размер очереди

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print("Is queue empty?", queue.isEmpty())
print("Dequeued item:", queue.dequeue())
print("Queue size:", queue.size())
print("Peek item:", queue.peek())
print("Dequeued item:", queue.dequeue())
print("Dequeued item:", queue.dequeue())
print("Is queue empty?", queue.isEmpty())

