# Assignment 1

# Q1. Conditional Statements - The If Statement:

# Task 1 - code

def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"
    
def main_q1():
    print(check_number(6))
    print(check_number(-2))
    print(check_number(0))

# Task 2 - understanding

# Inputs:
# The function check_number() receives an input called num and the function checks that number.

# Outputs:
# The function returns a message saying if the number's positive, negative, or zero.

# Main variables:
# num - the variable being evaluated

# Functions used:
# check_number() and it determines the sign of a number
# main_q1() and it runs some example tests

# Task 3 - Modification

# I changed the inputs

print(check_number(7))
print(check_number(-5))
print(check_number(0))

# Observation:
# The function correctly identified the sign of the number.


# Q2. For Loop - Making a Star Shape:

# Task 1 - code

def star_shape(rows):
    for e in range(1, rows + 1):
        print("*" * e)

def main_q2():
    star_shape(5)

# Task 2 - understanding

# Inputs:
# rows as in the number of rows for the star pattern.

# Outputs:
# The function prints a triangle made of stars.

# Main variables:
# rows - total rows of the triangle.
# e - loop counter that controls how many stars print.

# Functions used:
# star_shape() it prints the star pattern
# main_q2() it calls the function

# Task 3 - modification

# I changed the number of rows

print("Testing with 4 rows: ")
star_shape(4)

print("Testing with 6 rows: ")
star_shape(6)

# Observation:
# When you increase the rows, the triangle is larger.


# Q3. While Loop - Counting multiples of 3:

# Task 1 - code

def count_multiples(limit):
    x = 1
    while x <= limit:
        if x % 3 == 0:
            print("Multiple of 3")
        else:
            print(x)
        x += 1

def main_q3():
    count_multiples(12)

# Task 2 - understanding

# Inputs:
# limit is the number where the counting stops.

# Outputs:
# The function prints numbers from 1 to limit.
# When the number is divisible by 3, it prints "Multiple of 3".

# Main variables:
# x - counter variable
# limit - maximum number to count to

# Functions used:
# count_multiples() - performs the counting.
# main_q3() - calls the function.

# Task 3 - modification

# I tested different limits to see how the loop behaves.

print("Testing with limit = 6")
count_multiples(6)

print("Testing with limit = 19")
count_multiples(19)

# Observation:
# Every number divisible by 3 prints "Multiple of 3".


# Q4. Sum of Even Numbers in a Range:

# Task 1 - code

def sum_even(start, end):
    total = 0

    for t in range(start, end + 1):
        if t % 2 == 0:
            total += t

    return total

def main_q4():
    print(sum_even(1, 10))

# Task 2 - understanding

# Inputs:
# start is the starting number of the range
# end is the ending number of the range

# Outputs:
# the function returns the sum of all even numbers in that range.

# Main variables:
# total is the variable that keeps track of the running sum
# t is the loop variable used to check each number

# Functions used:
# sum_even() calculates the sum of even numbers
# main_q4() prints the result.

# Task 3 - modification

# I experimented with different ranges.

print(sum_even(1,10))
print(sum_even(60, 67))
print(sum_even(5,20))

# Observation:
# The function correctly adds only even numbers within the range


# Run all questions
if __name__ == "__main__":
    main_q1()
    main_q2()
    main_q3()
    main_q4()