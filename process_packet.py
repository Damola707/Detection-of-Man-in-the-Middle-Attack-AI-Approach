from scapy.all import sniff, IP, TCP, UDP
import joblib
import numpy as np
from sklearn.preprocessing import StandardScaler

# Load trained model and scaler
model = joblib.load("random_forest_model.pkl")
scaler = joblib.load("scaler.pkl")

def process_packet(packet):
    if IP in packet:
        ip_layer = packet[IP]
        proto = packet.proto

        src_ip = ip_layer.src
        dst_ip = ip_layer.dst

        # Initialize default ports
        sport, dport = 0, 0

        if TCP in packet:
            sport = packet[TCP].sport
            dport = packet[TCP].dport
        elif UDP in packet:
            sport = packet[UDP].sport
            dport = packet[UDP].dport

        # Example of adding more features to meet the 40-feature requirement
        packet_len = len(packet)  # Total packet length
        ttl = ip_layer.ttl  # Time to live
        src_ip_type = 1 if ip_layer.src.startswith('192') else 0  # Example: check for local network
        flags = packet.sprintf('%IP.flags%')  # Example of extracting flags (this is a placeholder)
        payload_size = len(packet.payload)  # Payload size
        timestamp = packet.time  # Timestamp of the packet
        ttl = ip_layer.ttl  # Time to live of the packet
        ip_version = ip_layer.version  # IPv4 or IPv6

        # Add more features here to reach 40, customizing as needed
        # For example, packet size, IP type (private/public), flags, protocol-related info, etc.
        
        # Create the feature vector: (Make sure it has 40 features in total)
        features = np.array([[sport, dport, proto, packet_len, ttl, src_ip_type, 
                             flags, payload_size, timestamp, ip_version]])

        # Apply scaling and predict
        features_scaled = scaler.transform(features)
        prediction = model.predict(features_scaled)

        label = "Malicious" if prediction[0] == 1 else "Benign"
        print(f"{src_ip}:{sport} -> {dst_ip}:{dport} | Prediction: {label}")

# Sniff packets from the network
sniff(prn=process_packet, filter="ip", store=0, count=50)
