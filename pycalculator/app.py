import streamlit as st
from math import factorial, sqrt, pow

def main():
    st.title("Multi-Tab Python Calculator")

    menu = ["Calculator", "Add Two Numbers", "Maximum of Two Numbers", "Factorial", "Simple Interest", "Compound Interest", "Check Armstrong Number", "Area of a Circle", "Prime Numbers in Interval", "Check Prime Number", "N-th Fibonacci Number", "Check Fibonacci Number", "N-th Multiple in Fibonacci", "ASCII Value of Character", "Sum of Squares of First N Natural Numbers", "Cube Sum of First N Natural Numbers"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Calculator":
        calculator()
    elif choice == "Add Two Numbers":
        add_two_numbers()
    elif choice == "Maximum of Two Numbers":
        max_two_numbers()
    elif choice == "Factorial":
        factorial_of_number()
    elif choice == "Simple Interest":
        simple_interest()
    elif choice == "Compound Interest":
        compound_interest()
    elif choice == "Check Armstrong Number":
        check_armstrong()
    elif choice == "Area of a Circle":
        area_of_circle()
    elif choice == "Prime Numbers in Interval":
        prime_numbers_interval()
    elif choice == "Check Prime Number":
        check_prime_number()
    elif choice == "N-th Fibonacci Number":
        nth_fibonacci()
    elif choice == "Check Fibonacci Number":
        check_fibonacci_number()
    elif choice == "N-th Multiple in Fibonacci":
        nth_multiple_in_fibonacci()
    elif choice == "ASCII Value of Character":
        ascii_value()
    elif choice == "Sum of Squares of First N Natural Numbers":
        sum_of_squares()
    elif choice == "Cube Sum of First N Natural Numbers":
        cube_sum()

def calculator():
    st.header("Calculator")
    num1 = st.number_input("Enter first number", format="%f")
    num2 = st.number_input("Enter second number", format="%f")
    operation = st.selectbox("Choose an operation", ["Add", "Subtract", "Multiply", "Divide"])
    
    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error! Division by zero."

    st.write("Result: ", result)

def add_two_numbers():
    st.header("Add Two Numbers")
    num1 = st.number_input("Enter first number", format="%f")
    num2 = st.number_input("Enter second number", format="%f")
    result = num1 + num2
    st.write("Result: ", result)

def max_two_numbers():
    st.header("Maximum of Two Numbers")
    num1 = st.number_input("Enter first number", format="%f")
    num2 = st.number_input("Enter second number", format="%f")
    result = max(num1, num2)
    st.write("Maximum: ", result)

def factorial_of_number():
    st.header("Factorial of a Number")
    num = st.number_input("Enter a number", min_value=0, step=1, format="%d")
    result = factorial(num)
    st.write("Factorial: ", result)

def simple_interest():
    st.header("Simple Interest")
    principal = st.number_input("Enter principal amount", format="%f")
    rate = st.number_input("Enter rate of interest", format="%f")
    time = st.number_input("Enter time period in years", format="%f")
    si = (principal * rate * time) / 100
    st.write("Simple Interest: ", si)

def compound_interest():
    st.header("Compound Interest")
    principal = st.number_input("Enter principal amount", format="%f")
    rate = st.number_input("Enter rate of interest", format="%f")
    time = st.number_input("Enter time period in years", format="%f")
    ci = principal * (pow((1 + rate / 100), time))
    st.write("Compound Interest: ", ci)

def check_armstrong():
    st.header("Check Armstrong Number")
    num = st.number_input("Enter a number", min_value=0, step=1, format="%d")
    sum = 0
    order = len(str(num))
    copy_num = num
    while copy_num > 0:
        digit = copy_num % 10
        sum += digit ** order
        copy_num //= 10
    if num == sum:
        st.write(num, "is an Armstrong number")
    else:
        st.write(num, "is not an Armstrong number")

def area_of_circle():
    st.header("Area of a Circle")
    radius = st.number_input("Enter radius of the circle", format="%f")
    area = 3.14159 * radius * radius
    st.write("Area: ", area)

def prime_numbers_interval():
    st.header("Prime Numbers in an Interval")
    start = st.number_input("Enter start of interval", min_value=0, step=1, format="%d")
    end = st.number_input("Enter end of interval", min_value=0, step=1, format="%d")
    primes = [num for num in range(start, end + 1) if all(num % div != 0 for div in range(2, int(sqrt(num)) + 1)) and num > 1]
    st.write("Prime numbers: ", primes)

def check_prime_number():
    st.header("Check Prime Number")
    num = st.number_input("Enter a number", min_value=0, step=1, format="%d")
    if num > 1 and all(num % div != 0 for div in range(2, int(sqrt(num)) + 1)):
        st.write(num, "is a prime number")
    else:
        st.write(num, "is not a prime number")

def nth_fibonacci():
    st.header("N-th Fibonacci Number")
    n = st.number_input("Enter n", min_value=0, step=1, format="%d")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    st.write("N-th Fibonacci number: ", a)

def check_fibonacci_number():
    st.header("Check if a Number is Fibonacci")
    num = st.number_input("Enter a number", min_value=0, step=1, format="%d")
    def is_perfect_square(x):
        s = int(sqrt(x))
        return s * s == x
    if is_perfect_square(5 * num * num + 4) or is_perfect_square(5 * num * num - 4):
        st.write(num, "is a Fibonacci number")
    else:
        st.write(num, "is not a Fibonacci number")

def nth_multiple_in_fibonacci():
    st.header("N-th Multiple of a Number in Fibonacci Series")
    k = st.number_input("Enter the multiple", min_value=1, step=1, format="%d")
    n = st.number_input("Enter n", min_value=1, step=1, format="%d")
    count = 0
    a, b = 0, 1
    while count < n:
        a, b = b, a + b
        if a % k == 0:
            count += 1
    st.write(f"The {n}-th multiple of {k} in Fibonacci series: ", a)

def ascii_value():
    st.header("ASCII Value of a Character")
    char = st.text_input("Enter a character", max_chars=1)
    if char:
        st.write("ASCII value: ", ord(char))

def sum_of_squares():
    st.header("Sum of Squares of First N Natural Numbers")
    n = st.number_input("Enter n", min_value=1, step=1, format="%d")
    result = n * (n + 1) * (2 * n + 1) // 6
    st.write("Sum of squares: ", result)

def cube_sum():
    st.header("Cube Sum of First N Natural Numbers")
    n = st.number_input("Enter n", min_value=1, step=1, format="%d")
    result = (n * (n + 1) // 2) ** 3
    st.write("Cube sum: ", result)

if __name__ == '__main__':
    main()
