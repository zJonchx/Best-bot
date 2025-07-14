import socket

def bypass(ip, port, time):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(time)
        sock.connect((ip, port))
        print("Bypass successful")
    except:
        print("Bypass failed")
    sock.close()

ip = input("Enter IP: ")
port = int(input("Enter port: "))
time = float(input("Enter timeout(s): "))

bypass(ip, port, time)
