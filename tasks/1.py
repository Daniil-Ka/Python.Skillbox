class OOP:
    def __init__(self, length=4):
        self.capacity = length
        self.length = 0
        self.val = [0] * length

    def get(self, index):
        return self.val[index]

    def set(self, index, value):
        self.val[index] = value

    def pop(self):
        if self.length <= 0:
            raise IndexError("Array is empty")
        last = self.val[self.length - 1]
        self.val[self.length - 1] = 0
        self.length -= 1

        if self.length * 3 < self.capacity:
            self.capacity //= 2
            self.val = self.val[::len(self.val) // 2]
        return last


    def push(self, value):
        if self.capacity <= self.length:
            new_capacity = self.capacity * 2
            new_value = [0] * new_capacity
            for i in range(len(self.val)):
                new_value[i] = self.val[i]
            self.val = new_value
            self.capacity = new_capacity
        self.val[self.length] = value
        self.length += 1

    def __str__(self):
        return str(self.val)

    def get_length(self):
        return self.length

    def get_capacity(self):
        return self.capacity