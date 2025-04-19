from scapy.all import sniff, IP, TCP, UDP
import numpy as np

def process_packet(packet):
    if IP in packet:
        ip_layer = packet[IP]
        proto = packet.proto
        sport, dport = 0, 0

        if TCP in packet:
            sport = packet[TCP].sport
            dport = packet[TCP].dport
        elif UDP in packet:
            sport = packet[UDP].sport
            dport = packet[UDP].dport

        # Additional features (sample)
        packet_len = len(packet)
        ttl = ip_layer.ttl
        payload_size = len(packet.payload)
        timestamp = packet.time

        # Example: Create the feature vector (expand this to match 40 features)
        features = np.array([[sport, dport, proto, packet_len, ttl, payload_size, timestamp]])

        print("Features: ", features)

# Test sniffing and feature extraction
sniff(prn=process_packet, filter="ip", store=0, count=10)
