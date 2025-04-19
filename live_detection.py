# MITM Detection: Live Model Inference
# This script loads the trained AI model and scaler to perform real-time or simulated detection on network traffic.
# Background: Demonstrates real-time intrusion detection based on AI classification.
# Covers concepts like false positives, detection accuracy, and latency trade-offs.

import joblib
from scapy.all import sniff, IP, TCP, ARP
import numpy as np
from datetime import datetime
import json
import os

# Load model and scaler
# Load trained Decision Tree model and StandardScaler
# These were saved after training on the labeled UNSW-NB15 dataset

model = joblib.load("random_forest_model.pkl")
scaler = joblib.load("scaler.pkl")\
    
# Simulated real-time detection:
# In practice, this would be a packet or flow feature vector extracted in real-time (e.g., via scapy or tshark)
# The features must be preprocessed exactly like the training data

ALERTS_FILE = "alerts.json"

def write_alert_to_file(alert_msg):
    if not os.path.exists(ALERTS_FILE):
        with open(ALERTS_FILE, 'w') as f:
            json.dump([], f)

    with open(ALERTS_FILE, 'r') as f:
        alerts = json.load(f)

    alerts.append(alert_msg)

    with open(ALERTS_FILE, 'w') as f:
        json.dump(alerts, f, indent=2)

def extract_features(pkt):
    if pkt.haslayer(IP) and pkt.haslayer(TCP):
        ip_layer = pkt[IP]
        tcp_layer = pkt[TCP]
        return [
            ip_layer.ttl,
            ip_layer.len,
            tcp_layer.sport,
            tcp_layer.dport,
            len(pkt)
        ]
    elif pkt.haslayer(ARP):
        return [
            int(pkt[ARP].op),
            int(pkt[ARP].hwlen),
            int(pkt[ARP].plen),
            sum(int(b) for b in pkt[ARP].psrc.split('.')),
            sum(int(b) for b in pkt[ARP].pdst.split('.'))
        ]
    return None

# Perform inference to detect if the current traffic is normal or a potential MITM attack
# Based on the AI model's decision boundary learned during training
def predict_packet(pkt):
    features = extract_features(pkt)
    if features:
        try:
            scaled = scaler.transform([features])
            prediction = model.predict(scaled)[0]
            if prediction == 1:
                alert_msg = f"[ALERT] {datetime.now()} | Suspicious Packet | Features: {features}"
                print(alert_msg)
                write_alert_to_file(alert_msg)
        except Exception as e:
            print(f"Prediction error: {e}")
            
# Log the results to simulate real-time intrusion alerts
# In an actual deployment, this would trigger a security event or alert
print("[+] Sniffing started...")
sniff(prn=predict_packet, store=0)
