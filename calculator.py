def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    return "Error: Division by zero"

if __name__ == "__main__":
    print("Addition 5 + 3 =", add(5, 3))
    print("Subtraction 5 - 3 =", subtract(5, 3))
    print("Multiplication 5 * 3 =", multiply(5, 3))
    print("Division 10 / 2 =", divide(10, 2))
