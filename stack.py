class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == [] # проверка на пустой стек

    def push(self, item):
        self.items.append(item) # добавляем элемент в стек

    def pop(self):
        return self.items.pop() # удаляем верхний элемент из стека

    def peek(self):
        return self.items[len(self.items) - 1] # вытаскиваем последний элемент

    def size(self):
        return len(self.items) # размер стека

stack = Stack()
stack.push('hello')
stack.push('true true true true true')
print("Top item:", stack.peek())
print("Is stack empty?", stack.isEmpty())
stack.pop()
print("Top item:", stack.peek())
print("Stack size:", stack.size())

