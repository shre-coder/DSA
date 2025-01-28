class PriorityQueue:
    def __init__(self):
        self.items = []

    def push(self, data, priority):
        index = 0
        while index < len(self.items) and self.items[index][1] <= priority:
            index += 1
        self.items.insert(index, (data, priority))

    def is_empty(self):
        return len(self.items) == 0

    def pop(self):
        if self.is_empty():
            raise IndexError("Priority Queue is empty")
        return self.items.pop(0)[0]

    def size(self):
        return len(self.items)


p = PriorityQueue()
p.push("A", 4)
p.push("B", 7)
p.push("C", 2)
p.push("D", 5)
p.push("E", 8)
p.push("F", 1)

while not p.is_empty():
    print(p.pop())
