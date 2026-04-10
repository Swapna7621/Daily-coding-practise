n = int(input("Enter a number of terms: "))
a = 0
b = 1
print("Fibonacci series:")
for i in rnge(n):
  print(a, end=" ")
  c = a + b
  a = b
  b = c
  
