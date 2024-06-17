# Your solution to Exercise 12
n = int(input("Enter the number n: "))

sum_of_three_digit_numbers = 0

for i in range(100, 1000):
    if i % n == 0:
        sum_of_three_digit_numbers += i

print(sum_of_three_digit_numbers)