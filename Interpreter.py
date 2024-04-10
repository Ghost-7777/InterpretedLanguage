
import sys

#read arguments
program_filepath = sys.argv[1]

#read file lines
program_lines = []
with open(program_filepath, "r") as program_file:
    program_lines = [line.strip() for line in program_file.readlines()]

program = []
token_counter = 0
label_tracker = {}
for line in program_lines:
    parts = line.split(" ")
    opcode = parts[0]

    #check for empty line
    if opcode == "":
        continue

    #check if its a label 
    if opcode.endswith(":"):
        label_tracker[opcode[:-1]] = token_counter
        continue

    #store opcode token
    program.append(opcode)
    token_counter += 1

    #handle each opcode
    if opcode == "PINS":
        #expect a number
        number = int(parts[1])
        program.append(number)
        token_counter += 1
    elif opcode == "SCORE":
        #prints and parse string literal
        string_literal = ' '.join(parts[1:])[1:-1]
        program.append(string_literal)
        token_counter += 1
    elif opcode == "RACK":
        #read label
        label = parts[1]
        program.append(label)
        token_counter += 1
    elif opcode == "AGAIN":
        #read label
        label = parts[1]
        program.append(label)
        token_counter += 1

class Stack:
    
    def __init__(self, size):
        self.buf = [0 for _ in range(size)]
        self.sp    = -1

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

while program[pc] != "HALT":
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
        if program_filepath in ["cat.txt", "helloworld.txt"]:
            value = input()
            stack.push(value)
        elif program_filepath == "multiply.txt":
            value = input()
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