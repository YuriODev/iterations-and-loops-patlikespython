n= int(input("Enter staircase steps number:     "))
for i in range(n):
  print(""*(n-i-1), end="")
  print("#"*(i+1))