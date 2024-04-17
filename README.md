# Bowling interpreter

Interpreter.py is a stack-based programming language that takes some bowling ideas and words and uses them to multiply integers and print strings.

| Instruction | Description |
| ------ | ------ |
| PINS | Pushes to top of stack |
| SCORE | Prints the string_literal |
| RACK | Jumps to label if top of the stack is 0 |
| RERACK | Jumps to label if top of stack is greater than 0 |
| MUL | Multiplies 2 numbers given by user |
| SUB | Pops 2 from the stack and subtracts the first from the second |
| MOVE | Pops from stack and returns it |
| BALL | Pops 2 from the stack and pushes the sum |
| HALT | Stops the interpreter after the value or string has been printed |
| REPEAT | Takes the users input for a string and input for how many times to repeat then repeats the string that many times. |
| REVERSE | Takes the users input for a string and then reverses the strings characters. |
