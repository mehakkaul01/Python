# # Take a single character as iput from the user. Check whether the character is an uppercase english letter (A-Z)

a = input("Enter a character: ")

if a >= 'A' and a <= 'Z':
    print("It is an uppercase english letter")
else:
    print("It is not an uppercase english letter")



# # Take three numbers from the user and determine which is the largest

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a == b == c:
    print("All numbers are equal")
elif a >= b and a >= c:
    print("First number is the largest")
elif b >= a and b >= c:
    print("Second number is the largest")
else:
    print("Third number is the largest")



# # Take a year as input and determine whether it is a leap year

year = int(input("Enter a year: "))

if year % 400 == 0:
    print("It is a leap year")

elif year % 4 == 0 and year % 100 != 0:
    print("It is a leap year")

else:
    print("It is not a leap year")



# # Take a number as input and determine whether it is a three digit number

number = int(input("Enter a number: "))
if number >= 100 and number <=999 or number >= -999 and number <= -100:
	print("It is a three digit number")
else:
	print("It is not a three digit number")



# # Take the traffic light colour as input and display the corresponding action

colour = input("Enter traffic light colour: ").lower
if colour == "red":
	print("Stop")
elif colour == "yellow":
	print("Wait")
elif colour == "green":
	print("Go")
else:
	print("Invalid Colour")


# Create a calculator that performs addition, subtraction multiplication and division based on the users choice

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Choose an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("Enter your choice (1-4): ")

if choice == "1":
    print("Result:", num1 + num2)
elif choice == "2":
    print("Result:", num1 - num2)
elif choice == "3":
    print("Result:", num1 * num2)
elif choice == "4":
    if num2 == 0:
        print("Error: cannot divide by zero")
    else:
        print("Result:", num1 / num2)
else:
    print("Invalid choice")
    



# Calculate the electricity bill according to these slabs:
# Units			Rate 
# 0-100			Rs2 per unit
# Units			Rate 
# 101-200			Rs 4 per unit
# Units			Rate 
# Above 200		Rs 6 per unit

units = int(input("Enter units consumed: "))

if units < 0:
    print("Invalid units")
elif units <= 100:
    bill = units * 2
    print("Total bill: Rs", bill)
elif units <= 200:
    bill = (100 * 2) + (units - 100) * 4
    print("Total bill: Rs", bill)
else:
    bill = (100 * 2) + (100 * 4) + (units - 200) * 6
    print("Total bill: Rs", bill)



# Calculate income tax based on annual income
# Example slabs:
# Upto 250000 - 0%
# Upto 250001 to 500000 - 5%
# 500001 to 1000000 - 20%
# Above 1000000 - 30%

income = float(input("Enter annual income: "))

if income < 0:
    print("Invalid income")
elif income <= 250000:
    tax = 0
elif income <= 500000:
    tax = income * 0.05
elif income <= 1000000:
    tax = income * 0.20
else:
    tax = income * 0.30

print("Income tax: Rs", tax)



# This program asks the user to enter a number, and then checks whether the number is even or odd. If the number is divisible by 2 (i.e., remainder is 0), it prints "It's an Even Number." Otherwise, it prints "It's an Odd Number."

a = int(input("Enter a number: "))
if a % 2 == 0:
	print("It's an even number")
else:
	print("It's an odd number")



# This program takes an integer input from the user and determines whether the number is positive, negative, or zero.

a = int(input("Enter a number:" ))
if a < 0:
	print("The number is negative")
elif a > 0:
	print("The number is positive")
else:
	print("The number is zero")



# This program asks the user to input their age and then classifies them into different categories: Child: If their age is 10 or below. Teenager: If their age is between 11 and 18. Adult: If their age is between 19 and 35. Senior: If their age is 36 or older.

age = int(input("Enter your age: "))

if age <= 10:
    print("Child")
elif age <= 18:
    print("Teenager")
elif age <= 35:
    print("Adult")
else:
    print("Senior")
    


# This program asks the user to input their score (between 0 and 100) and then gives the corresponding letter grade. A: 90–100 B: 80–89 C: 70–79 D: 60–69 F: Below 60

score = int(input("Enter your score (0-100): "))

if score < 0 or score > 100:
    print("Invalid score")
elif score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")



# This program asks the user to input a single letter and checks if it's a vowel (A, E, I, O, U) or a consonant. If the input is not a valid alphabet letter, it will print an error message.

ch = input("Enter a single letter: ")

if len(ch) != 1 or not ch.isalpha():
    print("Error: please enter a single alphabet letter")
elif ch.lower() in "aeiou":
    print("It's a vowel")
else:
    print("It's a consonant")



# This program simulates a simple login system. The user is asked to input a username and password. If both match the preset correct username and password, the program prints a success message. Otherwise, it prints an error message.

correct_username = "admin"
correct_password = "1234"

username = input("Enter username: ")
password = input("Enter password: ")

if username == correct_username and password == correct_password:
    print("Login successful!")
else:
    print("Error: incorrect username or password")



# This program asks the user to input three numbers and compares them. It prints which of the three numbers is the largest.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("The largest number is", a)
elif b >= a and b >= c:
    print("The largest number is", b)
else:
    print("The largest number is", c)



# This program asks the user to input a month number (1-12). It then tells the number of days in that month: January, March, May, July, August, October, December: 31 days April, June, September, November: 30 days February: 29 days (assuming a leap year)

month = int(input("Enter a month number (1-12): "))

if month in (1, 3, 5, 7, 8, 10, 12):
    print("31 days")
elif month in (4, 6, 9, 11):
    print("30 days")
elif month == 2:
    print("29 days (assuming a leap year)")
else:
    print("Invalid month. Enter a number between 1 and 12")



# Ask the user to enter the lengths of three sides of a triangle. Print whether it is:

# Equilateral (all three sides equal)
# Isosceles (exactly two sides equal)
# Scalene (all sides different) sol

a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

if a <= 0 or b <= 0 or c <= 0:
    print("Invalid input: sides must be positive")
elif a + b <= c or a + c <= b or b + c <= a:
    print("These sides cannot form a triangle")
elif a == b == c:
    print("Equilateral triangle")
elif a == b or b == c or a == c:
    print("Isosceles triangle")
else:
    print("Scalene triangle")
    


# Ask the user to enter their age. Print the ticket price:

# Below 5 years: Free
# 5 to 12 years: Rs 100
# 13 to 59 years: Rs 250
# 60 years and above: Rs 150	

age = int(input("Enter your age: "))

if age < 0:
    print("Invalid age")
elif age < 5:
    print("Ticket price: Free")
elif age <= 12:
    print("Ticket price: Rs 100")
elif age <= 59:
    print("Ticket price: Rs 250")
else:
    print("Ticket price: Rs 150")