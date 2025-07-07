import socket
import time

def send_udp_packets(ip, port, num_packets, duration=60):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    message = b'Test packet'
    start_time = time.time()
    sent_packets = 0

    while sent_packets < num_packets and (time.time() - start_time) < duration:
        try:
            sock.sendto(message, (ip, port))
            sent_packets += 1
            if sent_packets % 10000 == 0:
                print(f"{sent_packets} packets sent")
        except Exception as e:
            print(f"Error sending packet {sent_packets}: {e}")
            break

    sock.close()
    elapsed = time.time() - start_time
    print(f"Finished: Sent {sent_packets} packets to {ip}:{port} in {elapsed:.2f} seconds.")

if __name__ == "__main__":
    ip = input("Introduce la IP de destino: ")
    port = int(input("Introduce el puerto de destino: "))
    num_packets = int(input("Introduce el número de paquetes a enviar: "))
    try:
        duration = int(input("Introduce el tiempo máximo en segundos (por defecto 60): ") or "60")
    except ValueError:
        duration = 60

    send_udp_packets(ip, port, num_packets, duration)
