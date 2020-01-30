operatorList = []
operandList = []
index = 0

def cal():
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
 

        
