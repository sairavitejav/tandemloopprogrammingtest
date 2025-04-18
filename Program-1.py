# Name: Sai Ravi Teja Vudathala
# Program-1
''' Create a small calculator which performs operations such as Addition, Subtraction, Multiplication and Division using class.
 Calculator inputs :> ‘a’, ‘b’ and ‘type of operation’
 Datatype :> ‘a’ = double, ‘b’ = double, ‘type of operation’ = string '''

class Calculator():
    def __init__(self):
        self.a = 0
        self.b = 0
        self.operator = ''
        self.result = 0
    
    def get_input(self):
        self.a = float(input()) # Here I am using float, because the datatype of ‘a’ is double.
        # In Python, float is used to represent double precision floating point numbers.
        self.b = float(input())
        self.operator = input() # Here I am using string, because the datatype of ‘type of operation’ is string.
    
    def calculate(self):
        if self.operator == "+" or self.operator == "Addition":  # I am using both + and "Addition" to make it user-friendly.
            self.result = self.a + self.b
        elif self.operator == "-" or self.operator == "Subtraction":
            self.result = self.a - self.b
        elif self.operator == "*" or self.operator == "Multiplication":
            self.result = self.a * self.b
        elif self.operator == "/" or self.operator == "Division":
            # Check for division by zero
            if self.b == 0:
                print("Cannot divide by zero")
            else:
                self.result = self.a / self.b
        else:
            print("Invalid operator")
    
    def display_result(self):
        print(self.result)


result = Calculator() # Created an object of the class Calculator.

# Calling the methods of the class using the object created above.
result.get_input()
result.calculate()
result.display_result()
