while True:
    try:
     num1 = float(input("Enter the first number:"))
     num2 = float(input("Enter the second number"))

     result = num1/num2
    except ValueError:
       print("This is not a number")
    except ZeroDivisionError:
       print("can't divide by zero. please enter a non-zero number")
    else:
       print(f"Result:{num1}/{num2} = {result}")
       break
