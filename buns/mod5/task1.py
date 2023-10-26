class Node:
    """
    Вспомогательный класс для узлов списка
    """
    def __init__(self, data):
        self.data = data  # храним информацию
        self.nref = None  # ссылка на следующий узел
        self.pref = None  # Ссылка на предыдущий узел

class Stack:
    """
    Основной класс для стека
    """

    def __init__(self):
        self.end = None  # ссылка на конец стека

    def pop(self):
        """
        Возвращает и удаляет последний элемент из стека
        """
        if self.end is not None:
            val = self.end.data
            self.end = self.end.pref  # Сдвигаем указатель на предыдущий узел
            return val

    def push(self, val):
        """
        Добавляет элемент val в конец стека
        """
        new_node = Node(val)
        if self.end is None:
            self.end = new_node
        else:
            new_node.pref = self.end
            self.end = new_node

    def print(self):
        """
        Выводит содержимое стека
        """
        current = self.end
        while current:
            print(current.data, end=" ")
            current = current.pref
        print()

class Queue:
    """
    Основной класс для очереди
    """

    def __init__(self):
        self.start = None  # ссылка на начало очереди
        self.end = None  # ссылка на конец очереди

    def pop(self):
        """
        Возвращает и удаляет элемент val из начала очереди
        """
        if self.start is not None:
            val = self.start.data
            self.start = self.start.nref
            return val

    def push(self, val):
        """
        Добавляет элемент val в конец очереди
        """
        new_node = Node(val)
        if self.start is None:
            self.start = self.end = new_node
        else:
            self.end.nref = new_node
            new_node.pref = self.end
            self.end = new_node

    def insert(self, n, val):
        """
        Вставляет элемент val между элементами с номерами n-1 и n
        """
        new_node = Node(val)
        current = self.start
        count = 0

        if n == 0:
            new_node.nref = self.start
            self.start.pref = new_node
            self.start = new_node
        else:
            while current and count < n - 1:
                current = current.nref
                count += 1
            if current:
                new_node.nref = current.nref
                new_node.pref = current
                current.nref = new_node
                if new_node.nref:
                    new_node.nref.pref = new_node
                if current == self.end:
                    self.end = new_node

    def print(self):
        """
        Выводит содержимое очереди
        """
        current = self.start
        while current:
            print(current.data, end=" ")
            current = current.nref
        print()