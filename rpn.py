#Copyright (c) 2011 Andrew Gerber-Duffy
#
#Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import sys

def parse(line):
	"""
	Parses an RPN-formatted line of calculations.
	Note: all numbers and operators must be separated
	by a space
	"""
	nums = []
	
	ops = ['+', '-', '*', '/', '**']
	for i in line.split(" "):
		if i in ops:
			second = nums.pop()
			first  = nums.pop()
			nums.append(str(eval(first + i + second)))
		else:
			nums.append(i)
	return float(nums.pop())


def repl():
	"""
	Starts a REPL for rpncalc.
	Stack is limitless.
	"""
	stack = []
	operators = ['+', '-', '*', '/', '**']
	commands  = ['printstack', 'clearstack', 'exit']
	while True:
		line = str(raw_input("> ")).strip()
		answer = line

		line = line.split(" ")

		if line[0] in commands:
			eval(__handlecommand__(line[0], stack))

		elif line[-1] in operators and len(line) % 2 == 0:
			num = str(stack.pop())
			answer = eval(num + line[-1] + str(parse(" ".join(line[0:len(line)-1])))) 
		else:
			answer = str(parse(" ".join(line)))
		stack.append(answer)
		print answer

def __handlecommand__(command, stack):
	"""
	Handles a command, and returns a string that will adjust the
	'stack' accordingly
	"""
	if command == "printstack":
		print "Stack: "
		for num in stack:
			print num
		return "None"
	elif command == "exit":
		print
		print "Goodbye :)"
		sys.exit(0)
	elif command == "clearstack":
		return "stack = []"

def credits():
	print "Welcome to PyRPN! PyRPN is a console, stack-based RPN calculator"
	print "with a stack that is limited only by your computer's RAM."
	print "Enjoy!"
	print "-Andrew Gerber-Duffy"
	print

if __name__ == '__main__':
	credits()
	repl()


