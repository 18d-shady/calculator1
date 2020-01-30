operatorList = []
operandList = []
index = 0

def cal():
    """
    This simple caluclator helps you get the sum, difference, product and division of two
    Numbers. You may want to give it a try.
    """
    result = 0
    operatorList.clear()
    operandList.clear()
    s = input('>')
    if s == "":
        print('>')
    else:
        for char in s:
            if(char.isdigit()):
                operandList.append(int(char))
            elif char == " ":
                char.replace(" ", "")
            else:
                operatorList.append(char)

        if operatorList[0] == '+':
            result = operandList[0] + operandList[1]

        elif operatorList[0] == '-':
            result = operandList[0] - operandList[1]

        elif operatorList[0] == '*':
            result = operandList[0] * operandList[1]

        elif operatorList[0] == '/':
            result = operandList[0] / operandList[1]

        elif operatorList[0] == '=':
            result = operandList[0] = operandList[1]
            
        print(result)
        
while(True):
    cal()
 

        
