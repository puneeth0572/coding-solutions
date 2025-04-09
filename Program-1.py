
Problem 1: Calculator
Language: Python
Perform operations: Addition, Subtraction, Multiplication, Division
Input: a (double), b (double), operation (string)

class Calculator:
    def __init__(self, a, b, opeartion):
        self.a = a
        self.b = b
        self.operation = opeartion.lower()
    def calculate(self):
        if self.operation == 'add':
            return self.a + self.b
        elif self.operation == 'subtract':
            return self.a - self.b
        elif self.operation == 'multiply':
            return self.a * self.b
        elif self.operation == 'divide':
            if self.b == 0:
                return "Division by zero is not allowed"
            return self.a / self.b
        else:
            return "Invalid Operation. Please use 'addition','subtraction','multiplication','division'"
if __name__ == "__main__":
    print("Simple Calculator")
    print("Available operations: addition,subtraction,multiplications,division")
    
    try:
        a = float(input("Enter the first number(a): "))
        b = float(input("Enter the second number (b): "))
        op = input("Enter opeartion type: ")

        calc = Calculator(a, b, op)
        result = calc.calculate()
        print(f"\nResult of {op}: {a} and {b} = {result}")
    except ValueError:
        print("Please enter valid numbers for a and b")
         
