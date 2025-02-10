class Calculator:
    def __init__(self):
        self.choices = {0: "Exit", 1: "Addition", 2: "Subtraction", 3
                        : "Multiplication", 4: "Division", 5: "Exponentiation", 6: "Integer Division",7
                        :"Mean",8: "Median",9: "Mode",10: "Veriance",11: "Standard Deviation"}
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
    
    def mean(self,numbers):
        if not numbers:
            numbers = input("Enter numbers separated by space: ")
            numbers = [float(num) for num in numbers.split()]
        return sum(numbers) / len(numbers)
    
    def median(self):
        numbers = input("Enter numbers separated by space: ")
        numbers = [float(num) for num in numbers.split()]
        numbers.sort()
        n = len(numbers)
        if n % 2 == 0:
            return (numbers[n // 2 - 1] + numbers[n // 2]) /2
        else:
            return numbers[n // 2]
        
    def mode(self):
        numbers = input("Enter numbers separated by space: ")
        numbers = [float(num) for num in numbers.split()]
        numbers.sort()
        count_dict = { num: numbers.count(num) for num in numbers}
        return count_dict[max(count_dict.values())]
       
    def variance(self):
        numbers = input("Enter numbers separated by space: ")
        numbers = [float(num) for num in numbers.split()]
        n=len(numbers)
        mean_val = self.mean(numbers)
        variance = sum((x - mean_val) ** 2 for x in numbers) / n
        return variance
    
    def standard_deviation(self):
        variance = self.variance()
        return variance ** 0.5
            
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
                    print(f"Result: {round(self.add(),2)}")
                elif choice == 2:
                    print(f"Result: {round(self.subtract(),2)}")
                elif choice == 3:
                    print(f"Result:{round(self.multiply(),2)}")
                elif choice == 4:
                    print(f"Result: {round(self.divide(),2)}")
                elif choice == 5:
                    print(f"Result: {round(self.exponentiation(),2)}")
                elif choice == 6:
                    print(f"Result: {round(self.integer_division(),2)}")
                elif choice == 7:
                    print(f"Result: {round(self.mean(),2)}")
                elif choice == 8:
                    print(f"Result: {round(self.median(),2)}")
                elif choice == 9:
                    print( f"Result: {round(self.mode(),2)}")
                elif choice == 10:
                    print(f"Result: {round(self.variance(),2)}")
                elif choice == 11:
                    print(f"Result: {round(self.standard_deviation(),2)}")
                else:
                    break
            else:
                print("Invalid choice. Please choose a valid option.")

cal= Calculator()
cal.run()  
