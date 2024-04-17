import sys

# Read arguments
program_filepath = sys.argv[1]

# Read file lines
program_lines = []
with open(program_filepath, "r") as program_file:
    program_lines = [line.strip() for line in program_file.readlines()]

program = []
token_counter = 0
label_tracker = {}
for line in program_lines:
    parts = line.split(" ")
    opcode = parts[0]

    # Check for empty line
    if opcode == "":
        continue

    # Check if it's a label
    if opcode.endswith(":"):
        label_tracker[opcode[:-1]] = token_counter
        continue

    # Store opcode token
    program.append(opcode)
    token_counter += 1

    # Handle each opcode
    if opcode == "PINS":
        # Expect a number
        number = int(parts[1])
        program.append(number)
        token_counter += 1
    elif opcode == "SCORE":
        # Prints and parse string literal
        string_literal = ' '.join(parts[1:])[1:-1]
        program.append(string_literal)
        token_counter += 1
    elif opcode == "RACK":
        # Read label
        label = parts[1]
        program.append(label)
        token_counter += 1
    

class Stack:

    def __init__(self, size):
        self.buf = [0 for _ in range(size)]
        self.sp = -1

    def push(self, number):
        self.sp += 1
        self.buf[self.sp] = number

    def pop(self):
        number = self.buf[self.sp]
        self.sp -= 1
        return number

    def top(self):
        return self.buf[self.sp]


pc = 0
stack = Stack(256)

while pc < len(program) and program[pc] != "HALT":
    opcode = program[pc]
    pc += 1

    if opcode == "PINS":
        number = program[pc]
        pc += 1
        stack.push(number)
    elif opcode == "POP":
        stack.pop()
    elif opcode == "ADD":
        a = stack.pop()
        b = stack.pop()
        stack.push(a + b)
    elif opcode == "SUB":
        a = stack.pop()
        b = stack.pop()
        stack.push(b - a)
    elif opcode == "SCORE":
        value = stack.pop()
        if value == 0:
            value = program[pc]

        print(value)
    elif opcode == "READ":
        value = input()
        if program_filepath == "multiply.txt":
            try:
                value = int(value)
            except ValueError:
                print("Error: Please enter a valid integer.")
                continue  # Skip the rest of the loop iteration
        stack.push(value)
    elif opcode == "MUL":
        a = stack.pop()
        b = stack.pop()
        stack.push(a * b)
    elif opcode == "RACK":
        number = stack.top()
        if number == 0:
            pc = label_tracker[program[pc]]
        else:
            pc += 1
    elif opcode == "RERACK":
        number = stack.top()
        if number > 0:
            pc = label_tracker[program[pc]]
        else:
            pc += 1
    elif opcode == "REPEAT":
        string_to_repeat = input("Enter the word to repeat: ")
        repeat_count = int(input("Enter how many times to repeat: "))

        for _ in range(repeat_count):
            print(string_to_repeat)
    elif opcode == "REVERSE":
        string_to_reverse = stack.pop() 
        reversed_string = string_to_reverse[::-1]  
        print(reversed_string)  