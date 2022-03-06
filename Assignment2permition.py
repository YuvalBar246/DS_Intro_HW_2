def com_equation(equation):
    valid = "1234567890*/-+"
    valid_true = True
    ind = 0
    while ind < len(equation):
        ind += 1
        for i in equation:
            if i in valid:
                continue
            valid_true = False
            return "invalid input"
    if valid_true:
        calcul = eval(equation)
        if "." in str(calcul):        
            return str(calcul) + " (float)"
        else:
            return str(calcul) + " (int)"