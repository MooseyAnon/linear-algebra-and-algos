"""
Calculating expressions given as a string.

Question: calculate the expression "(5 * 4 + 3 * 12) - 1"

Two main steps:
    - covert to reverse polish notation (shunting yard algo)
    - RP calculator to find solution

This solution is intended to be for practice purposes and makes
the following assumtions about the input:
    - is a valid expression
    - no division by zero
    - there are spaces between each of the numbers/character
"""

def has_higher_presdicence(op1: str, op2: str) -> bool:
    """Check operator precidence."""
    return op1 in ("*", "/") and op2 in ("+", "-")


def calculate(num1: int, num2: int, op: str) -> int:
    """Do the operation that corresponds to the given string operator."""
    if op == "+": return num1 + num2
    if op == "-": return num1 - num2
    if op == "*": return num1 * num2
    if op == "/": return int(num1 / num2)


def shunting(exp: str) -> str:
    """Convert an infix experession to postfix (RP) notation."""
    
    stack: list[str] = []  # holds operators
    queue: list[str] = []  # holds numbers and final result
    
    tokens: list[str] = exp.split()
    operators: set[str] = {"+", "-", "*", "/"}
    
    for token in tokens:
        # handle opening bracket
        if token == "(":
            stack.append(token)
            continue
        
        # closing backet
        if token == ")":
            while stack and (item := stack.pop()) != "(":
                queue.append(item)
            continue
        
        # this is a number
        if token not in operators:
            queue.append(token)
            continue
        
        # handle operators
        # check if operator on top of stack has higher presidence than
        # current token
        if stack and has_higher_presdicence(stack[-1], token):
            # remove higher predicence token from stack
            queue.append(stack.pop())
        
        # add currenct opperator to stack
        stack.append(token)
    
    # add anything left over to the queue
    while stack:
        queue.append(stack.pop())
    
    return " ".join(queue)


def reverse_polish(exp: str) -> int:
    """Calculate the result of a reverse polish expression."""

    stack: list[int] = []  # hold the result of the calculation
    
    tokens: list[str] = exp.split()
    operators: set[str] = {"+", "-", "*", "/"}

    for token in tokens:
        # handle regular numbers
        if token not in operators:
            stack.append(int(token))
            continue

        # handle calculations, we need to ensure order as some operators
        # will return different results based on order
        b: str = stack.pop()
        a: str = stack.pop()
        stack.append(calculate(a, b, token))

    return stack.pop()


# expected: 5 4 * 3 12 * + 1 -
x = "( 5 * 4 + 3 * 12 ) - 1"

print(reverse_polish(shunting(x)))


# qucick test
assert shunting(x) == "5 4 * 3 12 * + 1 -"
assert reverse_polish(shunting(x)) == 55
