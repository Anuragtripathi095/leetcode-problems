class PeekingIterator:
    def __init__(self, iterator):
        self.iterator = iterator
        self.nextElement = iterator.next() if iterator.hasNext() else None

    def peek(self):
        return self.nextElement

    def next(self):
        current = self.nextElement
        self.nextElement = self.iterator.next() if self.iterator.hasNext() else None
        return current

    def hasNext(self):
        return self.nextElement is not None