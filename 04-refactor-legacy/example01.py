def calcThings(x, y, mode=None, extra=None):
    if mode == None:
        mode = "add"
    if mode == "add":
        if type(x) == str:
            try:
                x = int(x)
            except:
                x = 0
        if type(y) == str:
            try:
                y = int(y)
            except:
                y = 0
        result = x + y
    elif mode == "sub":
        if type(x) == str:
            try:
                x = int(x)
            except:
                x = 0
        if type(y) == str:
            try:
                y = int(y)
            except:
                y = 0
        result = x - y
    elif mode == "multi":
        if type(x) == str:
            try:
                x = int(x)
            except:
                x = 0
        if type(y) == str:
            try:
                y = int(y)
            except:
                y = 0
        result = x * y
    elif mode == "div":
        if y == 0 or y == "0":
            result = "Division by zero error!"
        else:
            try:
                result = int(x) / int(y)
            except:
                result = "Bad input"
    else:
        result = None
    if extra != None:
        if mode == "add":
            result = result + 10
        elif mode == "sub":
            result = result - 5
        else:
            result = result
    if result == None:
        print("Error")
    else:
        print("Result is: " + str(result))
    return result