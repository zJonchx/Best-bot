import socket
import time

def send_udp_packets(ip, port, pps, duration=60):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    message = b'Test packet'
    total_packets = pps * duration
    sent_packets = 0
    start_time = time.time()

    while (time.time() - start_time) < duration:
        second_start = time.time()
        packets_this_second = 0
        while packets_this_second < pps and (time.time() - start_time) < duration:
            try:
                sock.sendto(message, (ip, port))
                sent_packets += 1
                packets_this_second += 1
            except Exception as e:
                print(f"Error sending packet {sent_packets}: {e}")
                break
        elapsed = time.time() - second_start
        if elapsed < 1:
            time.sleep(1 - elapsed)

    sock.close()
    elapsed = time.time() - start_time
    print(f"Finished: Sent {sent_packets} packets to {ip}:{port} in {elapsed:.2f} seconds.")

if __name__ == "__main__":
    ip = input("Introduce la IP de destino: ")
    port = int(input("Introduce el puerto de destino: "))
    pps = int(input("Introduce la cantidad de paquetes por segundo (pps): "))
    try:
        duration = int(input("Introduce el tiempo máximo en segundos (por defecto 60): ") or "60")
    except ValueError:
        duration = 60

    send_udp_packets(ip, port, pps, duration)
