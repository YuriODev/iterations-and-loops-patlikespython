# Your solution to Exercise 26
n = int(input())

count = 0

for i in range(100, 1000):

    first_digit = i // 100
    second_digit = i // 10 % 10
    third_digit = i % 10

    sum_of_digits = first_digit + second_digit + third_digit

    if sum_of_digits == n:
        count += 1

print(count)