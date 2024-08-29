class BinaryNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

    def insert(self, data):
        if self.data < data:
            if self.right is None:
                self.right = BinaryNode(data)
            else:
                self.right.insert(data)
        else:
            if self.left is None:
                self.left = BinaryNode(data)
            else:
                self.left.insert(data)

# Создаем корневой узел
root = BinaryNode(10)
# Вставляем новые значения
root.insert(5)
root.insert(15)
root.insert(2)
root.insert(7)
root.insert(12)
root.insert(17)

# Печатаем дерево
print(root.left.right)  # Выведет: 5
print(root.right.left)  # Выведет: 7
print(root.right.right)  # Выведет: 12
print(root.left.left)  # Выведет: 2

# Печатаем значение корневого узла
print(root)  # Выведет: 10


