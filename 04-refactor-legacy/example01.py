def calculate(x, y, operation=None, extra=None):
    """
    Perform arithmetic operations (add, sub, multi, div) on x and y.
    Optionally modify result if extra is provided.
    """
    # Set default operation to 'add' if not specified
    if operation is None:
        operation = "add"

    # Helper function to safely convert string input to integer
    def to_int(val):
        if isinstance(val, str):
            try:
                return int(val)
            except Exception:
                return 0  # Fallback to 0 if conversion fails
        return val

    result = None  # Initialize result

    # Perform the requested arithmetic operation
    if operation == "add":
        x_int = to_int(x)
        y_int = to_int(y)
        result = x_int + y_int  # Addition
    elif operation == "sub":
        x_int = to_int(x)
        y_int = to_int(y)
        result = x_int - y_int  # Subtraction
    elif operation == "multi":
        x_int = to_int(x)
        y_int = to_int(y)
        result = x_int * y_int  # Multiplication
    elif operation == "div":
        # Check for division by zero
        if y == 0 or y == "0":
            result = "Division by zero error!"
        else:
            try:
                result = int(x) / int(y)  # Division
            except Exception:
                result = "Bad input"  # Handle invalid input

    # Optionally modify result if 'extra' is provided
    if extra is not None:
        if operation == "add" and isinstance(result, (int, float)):
            result += 10  # Add 10 for 'add' operation
        elif operation == "sub" and isinstance(result, (int, float)):
            result -= 5   # Subtract 5 for 'sub' operation

    # Print result or error message
    if result is None:
        print("Error")
    else:
        print(f"Result is: {result}")
    return result