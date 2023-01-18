# Author: Aubrey Floyd
# GitHub username: aubreyfloyd2
# Date: 1/18/2023
# Description: Asks the user for five numbers
#              and then outputs the average of the five numbers
print("Please enter five numbers.")
num_1 = float(input())
num_2 = float(input())
num_3 = float(input())
num_4 = float(input())
num_5 = float(input())
# get the sum of numbers and divide to get average
sum_total = (num_1 + num_2 + num_3 + num_4 + num_5)
avg = sum_total / 5
print("The average of those numbers is:")
print(avg)
