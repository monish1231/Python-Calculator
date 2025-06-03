# Basic calculator with simple math arithmetic operations
# Written for practice with Python as well user input concept, mini project

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if a == 0 or b == 0:
        return "Cannot divide by zero, Try Again;"
    return a / b

def calculator():
    print("\n--- Simple Calculator ---")    
    print("1. Add")
    print("2. Subtract") 
    print("3. Multiply")
    print("4. Divide")
    print("5. Quit")
    
    while True:
        try:
            choice = input("\nSelect operation (1-5): ")
            
            if choice == '5':
                print("See you buddy")
                break
                
            if choice not in ['1', '2', '3', '4']:
                print("Error... Try again.")
                continue
            
            # Get input i.e, number from user

            num1 = float(input("First number: "))
            num2 = float(input("Second number: "))
            
            # Do your calculation as such based on choice

            if choice == '1':
                result = add(num1, num2)
                op = '+'
            elif choice == '2':
                result = subtract(num1, num2)
                op = '-'
            elif choice == '3':
                result = multiply(num1, num2)
                op = '*'
            elif choice == '4':
                result = divide(num1, num2)
                op = '/'
            
            print(f"Result: {num1} {op} {num2} = {result}")
            
        except ValueError:
            print("Invalid input, Enter numbers only :(")
        except KeyboardInterrupt:
            print("\nNice interacting with you, Goodbye:)")
            break

if __name__ == "__main__":
    calculator()
