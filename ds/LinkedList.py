class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    def later_node(self, i):
        if i == 0:
            return self
        return self.next.later_node(i - 1)

    def __del__(self):
        print(f"{self.value} got deleted")

class LinkedList:
    def __init__(self, iterable):
        self.head = None
        self.size = 0
        self.build(iterable)

    def build(self, iterable):
        for value in reversed(iterable):
            self.insert_first(value)

    def delete_first(self):
        if self.head is not None:
            self.head = self.head.next
            self.size -= 1

    def insert_first(self, value):
        node = LinkedListNode(value)
        node.next = self.head
        self.head = node
        self.size += 1

    def insert_at(self, i, value):
        if i == 0:
            return self.insert_first(LinkedListNode(value))
        before_node = self.head.later_node(i-1)
        new_node = LinkedListNode(value)
        new_node.next = before_node.next
        before_node.next = new_node

    def __len__(self):
        return self.size

    def __repr__(self):
        values = []
        node = self.head
        while node is not None:
            values.append(node.value)
            node = node.next
        return f"LinkedList({', '.join(str(value) for value in values)})"

l = LinkedList([1, 2, 3])
l.insert_first(10)
            
