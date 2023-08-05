def division(num1, num2):
    try:
        quot = int(num1)/int(num2)
    except ZeroDivisionError:
        print("Zero Division Error: can't divide by 0")
    except ValueError:
        print("Value Error.")
    else:
        return quot

print("Try 1")
print("\n", division(10, 2))
print("\n\n")

print("Try 2")
print("\n", division('a', 3))
print("\n\n")

print("Try 3")
print("\n", division(5, 0))
