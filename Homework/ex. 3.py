def divide_numbers(dividend, divisor, M):
    try:
        result = dividend / divisor
        
        if result > M:
            raise ArithmeticError(f"The result {result} exceeds the allowed threshold {M}.")
        
        return result

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ArithmeticError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

dividend = float(input("Enter the dividend: "))
divisor = float(input("Enter the divisor: "))
M = float(input("Enter the threshold M: "))

result = divide_numbers(dividend, divisor, M)
if result is not None:
    print(f"The result of division is: {result}")
