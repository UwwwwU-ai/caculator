import sys

def main():
    if sys.argv[1] == "add":
        print(add(int(sys.argv[2]), int(sys.argv[3])))
    elif sys.argv[1] == "subtract":
        print(subtract(int(sys.argv[2]), int(sys.argv[3])))
    elif sys.argv[1] == "multiply":
        print(multiply(int(sys.argv[2]), int(sys.argv[3])))
    elif sys.argv[1] == "divide":
        print(divide(int(sys.argv[2]), int(sys.argv[3])))

def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b




if __name__ == "__main__":
    main()
