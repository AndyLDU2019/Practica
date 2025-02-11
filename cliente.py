import socket

def iniciar_cliente():
    # Crear un socket TCP/IP
    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Definir la dirección y el puerto del servidor
    host = '127.0.0.1'
    puerto = 12345

    # Conectar al servidor
    cliente_socket.connect((host, puerto))
    print(f"Conectado al servidor en {host}:{puerto}")

    # Enviar datos al servidor
    mensaje = "Hola, servidor. Este es el cliente."
    cliente_socket.sendall(mensaje.encode('utf-8'))

    # Recibir la respuesta del servidor
    datos = cliente_socket.recv(1024)
    print(f"Recibido: {datos.decode('utf-8')}")

    # Cerrar la conexión
    cliente_socket.close()
    print("Conexión cerrada.")

if __name__ == "__main__":
    iniciar_cliente()
    #cambio estoy practicando
    #hola hola