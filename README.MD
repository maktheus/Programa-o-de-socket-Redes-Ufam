# Projeto de Operações Matemáticas Cliente-Servidor

Este projeto implementa uma comunicação básica entre cliente e servidor usando sockets TCP em Python. O servidor é capaz de realizar operações matemáticas simples (+, -, *, /) com base nas instruções recebidas do cliente, e retorna o resultado para o cliente.

## Funcionalidades

- **Servidor**: Aguarda conexões de clientes, recebe operações matemáticas e dois números, executa a operação, e envia o resultado de volta ao cliente.
- **Cliente**: Permite ao usuário escolher uma operação matemática e enviar dois números ao servidor, recebendo e imprimindo o resultado da operação.

## Como executar

### Requisitos

- Python 3.x

### Instruções

1. **Clone o repositório**:
```
git clone https://github.com/maktheus/Programa-o-de-socket-Redes-Ufam.git
```

2. **Execute o servidor**:
- Abra um terminal.
- Navegue até o diretório do projeto.
- Execute o comando:
  ```
  python servidor.py
  ```
- O servidor começará a ouvir conexões na porta 12345.

3. **Execute o cliente**:
- Abra um novo terminal.
- Navegue até o diretório do projeto.
- Execute o comando:
  ```
  python cliente.py
  ```
- Siga as instruções na tela para escolher uma operação e informar os números.

### Exemplo de Uso

No cliente, você será solicitado a escolher uma operação e informar dois números:

```
Escolha a operação (+, -, *, /): +
Informe o primeiro número: 5
Informe o segundo número: 3
```


O resultado aparecerá no cliente:

```
Resultado: 8
```


## Tecnologias Utilizadas

- Python 3.x: Linguagem de programação.
- Sockets TCP: Mecanismo de comunicação de rede para estabelecer a comunicação cliente-servidor.

## Autor

- Uchoa(maktheus)

## Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

made with ☕ and ❤️
