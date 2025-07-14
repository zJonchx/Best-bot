import socket

def bypass(ip, port, time):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(time)
    result = sock.connect_ex((ip, port))
    if result == 0:
        print("Bypass successful")
    else:
        print("Bypass failed")
    sock.close()

ip = input("Enter IP: ")
port = int(input("Enter port: "))
time = float(input("Enter timeout(s): "))

bypass(ip, port, time)
