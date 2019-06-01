'''
https://leetcode.com/problems/evaluate-reverse-polish-notation/

Evaluate the value of an arithmetic expression in Reverse Polish Notation.
Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Note:
Division between two integers should truncate toward zero.
The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be any divide by zero operation.
'''

class Solution:
	def evalRPN(self, tokens: List[str]) -> int:
		stack = list()
		ops = ['+', '-', '*', '/']
		for i in range(len(tokens)):
			item = tokens[i]
			if item in ops:
				stack.append(self.operate(item, stack))
			else:
				stack.append(int(item))
		return stack.pop()
				
				
	def operate(self, op, terms):
		y = terms.pop()
		x = terms.pop()
		if op == '+':
			return x + y
		elif op == '-':
			return x-y
		elif op == '*':
			return x*y
		elif op == '/':
			return int(x/y)