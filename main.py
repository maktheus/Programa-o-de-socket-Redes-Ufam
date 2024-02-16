from serverSide import handle_operation
import socket

def main():
    host = 'localhost'
    port = 12345
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print("🔎 Aguardando conexão...")

    while True:
        client_socket, address = server_socket.accept()
        print(f"✅ Conexão estabelecida com {address}")
        
        data = client_socket.recv(1024).decode('utf-8')
        operation, num1, num2 = data.split()
        num1, num2 = float(num1), float(num2)
        
        result = handle_operation(operation, num1, num2)
        
       
        if operation == '+':
            result_message = f"➕ Resultado: {result}"
        elif operation == '-':
            result_message = f"➖ Resultado: {result}"
        elif operation == '*':
            result_message = f"✖️ Resultado: {result}"
        elif operation == '/':
            result_message = f"➗ Resultado: {result}"
        else:
            result_message = "❌ Operação inválida."
        
        client_socket.send(result_message.encode('utf-8'))
        
        client_socket.close()

if __name__ == "__main__":
    main()
