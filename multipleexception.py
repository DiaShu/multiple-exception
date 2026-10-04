try:
    num1 = int(input("please enter a number here"))
    num2 = int(input("please enter another number here"))
    result = num1/num2
    result2 = num1+num2
    print("the result is", result)
    print("the result is", result2)

except ZeroDivisionError:
    print("Please replace 0 by another number")
except ValueError:
    print("Please retry with a vald number")
except NameError:
    print("Please check if all your variables are defined")

finally:
    print("this will run no matter what")