#write menu driven python program using class to build a calculator which can perform 
# 1. addition, 2. subtraction, 3. multiplication 4. division 5. Exponentiation 6, Integer Division 
class Calculator:
    def __init__(self):
        self.choices = {1: "Addition", 2: "Subtraction", 3
                        : "Multiplication", 4: "Division", 5: "Exponentiation", 6: "Integer Division", 7: "Exit" }
        self.choices_list = list(self.choices.keys())
        
    def add(self):
        num1 = float(input('Enter first number: '))
        num2 = float(input('Enter second number: '))
        return num1 + num2
    
    def subtract(self):
        num1 = float(input('Enter first number: '))
        num2 = float(input('Enter second number: '))
        return num1 - num2
    
    def multiply(self):
        num1 = float(input('Enter first number: '))
        num2 = float(input('Enter second number: '))
        return num1 * num2
    
    def divide(self):
        num1 = float(input('Enter first number: '))
        num2 = float(input('Enter second number: '))
        if num2 == 0:
            return "Error! Division by zero is not allowed"
        return num1 / num2
    
    def exponentiation(self):
        num1 = float(input('Enter first number: '))
        num2 = float(input('Enter second number: '))
        return num1 ** num2
    
    def integer_division(self):
        num1 = float(input('Enter first number: '))
        num2 = float(input('Enter second number: '))
        if num2 == 0:
            return "Error! Division by zero is not allowed"
        return num1 // num2
    
    def display_menu(self):
        print("\nCalculator Menu:")
        for key, value in self.choices.items():
            print(f"{key}. {value}")

    def run(self):
        while True:
            self.display_menu()
            choice = int(input('Enter Your Choice: '))
            if choice in self.choices_list:
                if choice == 1:
                    print(f"Result: {self.add()}")
                elif choice == 2:
                    print(f"Result: {self.subtract()}")
                elif choice == 3:
                    print(f"Result:{self.multiply()}")
                elif choice == 4:
                    print(f"Result: {self.divide()}")
                elif choice == 5:
                    print(f"Result: {self.exponentiation()}")
                elif choice == 6:
                    print(f"Result: {self.integer_division()}")
                else:
                    break
            else:
                print("Invalid choice. Please choose a valid option.")


cal= Calculator()
cal.run()  
