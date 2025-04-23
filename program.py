1: Write a python program to add all the odd numbers from 0 to 20.

# Initialize a variable to hold the sum of odd numbers
sum_of_odds = 0

# Loop through numbers from 0 to 20
for number in range(21):  # range(21) goes from 0 to 20 inclusive
    if number % 2 != 0:  # Check if the number is odd
        sum_of_odds += number  # Add the odd number to the sum

# Print the result
print("The sum of all odd numbers from 0 to 20 is:", sum_of_odds)
