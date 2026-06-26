# one queue

'''
push(1), [1]
push(2), [1,2] => [2,1]
push(3), [2,1,3] => [1,3,2] => [3,2,1]
push(4), [3,2,1,4] => switch 3 time to get [4,3,2,1]
push(5), [4,3,2,1,5] => switch 4 time to get [5,4,3,2,1]
'''
class Stack:

    def __init__(self):
        self._queue = collections.deque()

    def push(self, x):
        q = self._queue
        q.append(x)
        for _ in range(len(q) - 1):
            q.append(q.popleft())
        
    def pop(self):
        return self._queue.popleft()

    def top(self):
        return self._queue[0]
    
    def empty(self):
        return not len(self._queue)

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

############

from collections import deque

# two queues
class MyStack:

	def __init__(self):
		self.q1 = deque()
		self.q2 = deque()

	def push(self, x: int) -> None:
		self.q1.append(x)

	def pop(self) -> int:
		while len(self.q1) != 1:
			self.q2.append(self.q1.popleft())

		val = self.q1.popleft()
		self.q1, self.q2 = self.q2, self.q1
		return val

	def top(self) -> int:
		while len(self.q1) != 1:
			self.q2.append(self.q1.popleft())

        # tried to re-use while part, but seems not achievable, since val is retrieved in-between 
		val = self.q1[0]
		self.q2.append(self.q1.popleft())  # note: add back to q2, so q1 will always be empty

		self.q1, self.q2 = self.q2, self.q1
		return val


	def empty(self) -> bool:
		return not self.q1

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()