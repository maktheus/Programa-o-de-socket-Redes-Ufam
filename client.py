import socket

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = 'localhost'
    port = 12345
    
    client_socket.connect((host, port))
    
    print("Conectado ao servidor! 🌐")
    operation = input("Escolha a operação (+, -, *, /): ")
    num1 = input("Informe o primeiro número: ")
    num2 = input("Informe o segundo número: ")
    
    message = f"{operation} {num1} {num2}"
    client_socket.send(message.encode('utf-8'))
    
    result = client_socket.recv(1024).decode('utf-8')
    print(f"Resultado: {result} 📊")
    
    client_socket.close()
    print("Conexão encerrada. 👋")

if __name__ == "__main__":
    main()
