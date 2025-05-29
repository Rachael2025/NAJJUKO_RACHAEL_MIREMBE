from functools import reduce

numbers = [1,2,3,4,5]

factorial = lambda n: reduce(lambda x,y: x*y, range(1,n+1),1)

for num in numbers:
 print(f"factorial of {num} is {factorial(num)}")