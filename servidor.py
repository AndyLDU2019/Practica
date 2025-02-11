import socket

def iniciar_servidor():
    # Crear un socket TCP/IP
    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Obtener el nombre de la máquina local
    host = '127.0.0.1'
    puerto = 12345

    # Enlazar el socket al puerto
    servidor_socket.bind((host, puerto))

    # Escuchar conexiones entrantes
    servidor_socket.listen(1)
    print(f"Servidor escuchando en {host}:{puerto}...")

    while True:
        # Esperar una conexión
        print("Esperando una conexión...")
        cliente_socket, direccion = servidor_socket.accept()
        print(f"Conexión establecida con {direccion}")

        # Recibir datos del cliente
        datos = cliente_socket.recv(1024)
        print(f"Recibido: {datos.decode('utf-8')}")

        # Enviar una respuesta al cliente
        mensaje = "Hola, cliente. Mensaje recibido."
        cliente_socket.sendall(mensaje.encode('utf-8'))

        # Cerrar la conexión con el cliente
        cliente_socket.close()
        print("Conexión cerrada con el cliente.")

if __name__ == "__main__":
    iniciar_servidor()