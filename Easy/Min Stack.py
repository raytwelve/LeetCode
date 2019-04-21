'''
https://leetcode.com/problems/min-stack/

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
'''

class MinStack:
	stack = None
	def __init__(self):
		"""
		initialize your data structure here.
		"""
		self.stack = list()
		

	def push(self, x: int) -> None:
		if len(self.stack) == 0:
			self.stack.append((x,x))
		else:
			minimum = self.stack[-1][1]
			minimum = min(x, minimum)
			self.stack.append((x, minimum))

	def pop(self) -> None:
		self.stack.pop()		

	def top(self) -> int:
		return self.stack[-1][0]
		

	def getMin(self) -> int:
		# mini = 99999999
		# for n in self.stack:
		#	 if n < mini:
		#		 mini = n
		# return mini
		
		return(self.stack[-1][1])


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()