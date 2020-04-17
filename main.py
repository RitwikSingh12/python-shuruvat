def calculator(a,b,operator):
    if(operator == "+"):
        return a + b
        
    elif (operator == "-"):
        return a - b

    else:
        return "invalid operator"
        
a = int(input("pehla number\n"))
b = int(input("dusra number\n"))
operator = input("1. write + for addition \n 2. write - for subtraction")
#print("you chose" + str(a) + str(operator) + str(b))
answer = calculator(a,b,operator)
print(answer)