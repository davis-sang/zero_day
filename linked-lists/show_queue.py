from queue_1 import Queue

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print("Dequeue:", q.dequeue())  # Output: 1
print("Dequeue:", q.dequeue())  # Output: 2
q.enqueue(4)
print("Dequeue:", q.dequeue())  # Output: 3
print("Dequeue:", q.dequeue())  # Output: 4
