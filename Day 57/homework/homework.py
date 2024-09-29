# დავალება 1: 
def calculator():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Enter operation (add/subtract/multiply/divide): ")
    
    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        result = num1 / num2 if num2 != 0 else "Error: Division by zero"
    else:
        result = "Invalid operation"
    
    print(f"Result: {result}")



# დავალება 2: 
def sum_of_list():
    numbers = [1, 2, 3, 4, 5]
    return sum(numbers)



# დავალება 3: 
def average_of_list():
    numbers = [1, 2, 3, 4, 5]
    return sum(numbers) / len(numbers)



# დავალება 4:
def odd_or_even():
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")



# დავალება 5:
def time_travel():
    current_age = int(input("Enter your current age: "))
    current_year = int(input("Enter the current year: "))
    travel_years = int(input("Enter how many years you want to travel: "))
    direction = input("Do you want to travel to the past or future? (past/future): ")
    
    if direction == "future":
        future_year = current_year + travel_years
        future_age = current_age + travel_years
    else:
        future_year = current_year - travel_years
        future_age = current_age - travel_years
    
    print(f"After time travel, it will be the year {future_year} and you will be {future_age} years old.")




# დავალება 6:
def add_one():
    number = int(input("Enter a number: "))
    result = number + 1
    print(f"Result: {result}")



# დავალება 7 
def awesome_check():
    num = float(input("Enter a number: "))
    return "Awesome!" if num > 10 else "Not awesome enough!"



# დავალება 8 
def smaller_digit():
    digit1 = int(input("Enter first digit: "))
    digit2 = int(input("Enter second digit: "))
    return min(digit1, digit2)



# დავალება 9 
def text_length():
    text = input("Enter some text: ")
    return len(text)



# დავალება 10 
def sum_two_numbers():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    return num1 + num2


# დავალება 11 
def positive_or_negative():
    num = float(input("Enter a number: "))
    return "Positive" if num > 0 else "Negative" if num < 0 else "Zero"



# დავალება 12 
def is_even():
    num = int(input("Enter a number: "))
    return num % 2 == 0



# დავალება 13 
def sum_plus_five():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    return num1 + num2 + 5




# ფუნქციების გატესტვა
calculator()
print(f"Sum of list: {sum_of_list()}")
print(f"Average of list: {average_of_list()}")
odd_or_even()
time_travel()
add_one()
print(awesome_check())
print(smaller_digit())
print(text_length())
print(sum_two_numbers())
print(positive_or_negative())
print(is_even())
print(sum_plus_five())
