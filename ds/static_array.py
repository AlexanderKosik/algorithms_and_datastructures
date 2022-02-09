# Sequence Interface:
# Container: build(), len()
# Static: get_at(), set_at(), iter()


class StaticArraySequence:
    """
    Order is extrinsic
    """
    def __init__(self, other):
        # O(n)
        self._container = [x for x in other]
        self.size = len(self._container)

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
