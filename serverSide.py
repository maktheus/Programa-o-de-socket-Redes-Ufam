import socket

def handle_operation(operation, num1, num2):
    if operation == '+':
        return f"{num1 + num2} ➕"
    elif operation == '-':
        return f"{num1 - num2} ➖"
    elif operation == '*':
        return f"{num1 * num2} ✖️"
    elif operation == '/':
        if num2 != 0:
            return f"{num1 / num2} ➗"
        else:
            return "Erro: Divisão por zero. ❌"
    else:
        return "Operação inválida. ⚠️"
