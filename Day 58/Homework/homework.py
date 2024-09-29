#დავალება 1

def get_larger_number(num1, num2):
    return max(num1, num2)


first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

result = get_larger_number(first_number, second_number)
print(f"The larger number is: {result}")





# დავალება 2
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"



num = int(input("Enter a number: "))
result = check_even_odd(num)
print(f"The number {num} is {result}")





# დავალება 3
def greet_user(name):
    print(f"Hello {name}!")

# Example usage:
user_name = input("Enter your name: ")
greet_user(user_name)




#დავალება 4
def check_guess(secret_number, user_guess):
    if user_guess == secret_number:
        print("Correct, well done!")
    else:
        print("Incorrect, try again.")

# Example usage:
secret = 42
guess = int(input("Guess the number: "))
check_guess(secret, guess)
