class Queue(object):
    def __init__(self):
        self._queue = []

    def insert(self, element):
        if not element in self._queue:
            self._queue.append(element)
            
    def remove(self):
        try:
            return self._queue.pop(0)
        except:
            raise ValueError()

queue = Queue()
queue.insert(5)
queue.insert(6)
print queue.remove()

queue.insert(7)
print queue.remove()

print queue.remove()

print queue.remove()