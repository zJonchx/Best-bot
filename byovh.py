import socket

def bypass(ip, port, time):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    start_time = time.time()
    data = "hello"  # Los datos que se van a enviar

    while time.time() - start_time < time:
        result = sock.sendto(data.encode(), (ip, port))  # intenta enviar los datos
    sock.close()
    
    if result: 
        print("Bypass successful")
    else:
        print("Bypass failed")
   
ip = input("Enter IP: ")
port = int(input("Enter port: "))
time = float(input("Enter timeout(s): "))

bypass(ip, port, time)
