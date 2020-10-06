"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )
                    

# Replace this with your code
while True:
    user_input = input() # "+ 3 5"
    tokens = user_input.split(" ") # ["+", "3", "5"]
    if tokens[0] == "q":
        break
    elif tokens[0] == "+":
       print(add(float(tokens[1]), float(tokens[2])))
       break
    elif tokens[0] == "-":
        print(subtract(float(tokens[1]), float(tokens[2])))
        break
    elif tokens[0] == "*":
        print(multiply(float(tokens[1]), float(tokens[2])))
        break
    elif tokens[0] == "/":
        print(divide(float(tokens[1]), float(tokens[2])))
        break
    elif tokens[0] == "square":
        print(square(float(tokens[1])))
        break
    elif tokens[0] == "cube":
        print(cube(float(tokens[1])))
        break
    elif tokens[0] == "power":
        print(power(float(tokens[1]), float(tokens[2])))
        break
    else:
        print(mod(float(tokens[1]), float(tokens[2])))
        break



