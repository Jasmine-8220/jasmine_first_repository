length= int(input("How many terms? "))

n1, n2 = 0, 1
count = 0

if length <= 0:
   print("Please enter a positive integer")

elif length == 1:
   print("Fibonacci sequence upto",length,":")
   print(n1)

else:
   print("Fibonacci sequence:")
   while count < length:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1