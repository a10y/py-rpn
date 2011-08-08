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
			nums.append(str(eval(nums.pop() + i + nums.pop())))
		else:
			nums.append(i)
	return float(nums.pop())

def repl():
	"""
	Starts a REPL for rpncalc.
	Stack is limitless.
	"""
	stack = []
	
	while True:
		line = str(raw_input("> "))
	
		operators = ['+', '-', '*', '/', '**']
		commands  = ['printstack', 'exit']
		answer = line
		if line[-1] in operators:
			num = str(stack.pop())
			answer = eval(line+num)
			print answer

		stack.append(answer)

def credits():
	print "Welcome to PyRPN! PyRPN is a console, stack-based RPN calculator"
	print "with a stack that is limited only by your computer's RAM."
	print "Enjoy!"
	print "-Andrew Gerber-Duffy"
	print

if __name__ == '__main__':
	credits()
	repl()


