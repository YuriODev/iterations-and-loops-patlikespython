# Your solution to Exercise 9
a=int(input("Enter a number:  "))
b=int(input("Enter another number:  "))
c=int(input("Enter the multiple:   "))
for i in range(a,b+1):
    if i % c ==0:
        print(i)