# Sequence Interface:
# Container: build(), len()
# Static: get_at(), set_at(), iter()
# Dynamic: insert_at(), delete_at(), insert_first(), insert_last()


class DynamicArraySequence:
    """
    Order is extrinsic
    """
    def __init__(self, other):
        self.build(other)

    def build(self, other):
        self._container = [x for x in other] # O(n)
        self.size = len(self._container)

    def insert_at(self, i, value):
        new_container = self._container[:i] + [value] + self._container[i:] # O(n)
        self.build(new_container)

    def delete_at(self, i):
        new_container = self._container[:i] + self._container[i+1:] # O(n)
        self.build(new_container)

    def insert_first(self, value):
        self.insert_at(0, value) # O(n)

    def insert_last(self, value):
        self.insert_at(self.size, value) # O(n)

    def delete_first(self):
        self.delete_at(0)

    def delete_last(self):
        self.delete_at(self.size-1)

    def get_at(self, i):
        try:
            return self._container[i] # O(1)
        except IndexError:
            raise

    def set_at(self, i, value):
        try:
            self._container[i] = value # O(1)
        except IndexError:
            raise

    def __len__(self):
        return self.size

    def __iter__(self):
        yield from self._container

    def __repr__(self):
        return repr(self._container)
