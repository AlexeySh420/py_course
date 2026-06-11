# Lab Queue

class Queue:
    def __init__(self):
        self._queue = []

    def put(self, value):
        self._queue.append(value)
        print("Adding", value)

    def get(self):
        if not self._queue:
            raise IndexError("Queue is empty")
        value = self._queue.pop(0)
        print("removed the element", value)
        return value

    def __str__(self):
        return f'{self._queue}'


que = Queue()
que.put(1)
que.put('dog')
que.put(False)


try:
    for i in range(4):
        print(que.get())
except Exception as e:
    print('Queue error:', e)