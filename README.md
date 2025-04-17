# Detection of Man-in-the-Middle Attack: AI Approach

## Objective
To simulate the detection of Man-in-the-Middle (MitM) attacks using AI-based techniques that analyse network traffic patterns and classify anomalies in real time.

## Simulation Type
Network Security Simulation / AI-based Anomaly Detection

## Types of Dataset
1. Packet captures (PCAP)
2. NetFlow data
3. TCP/IP metadata
4. traffic logs (normal and MitM infected)
5. time-series features

## Possible Sources for Dataset
1. CICIDS 2017
2. TON_IoT dataset
3. UNSW-NB15
4. MIT Lincoln Lab DARPA dataset
5. Kaggle

## Dataset URLs
1. https://www.unb.ca/cic/datasets/ids-2017.html
2. https://research.unsw.edu.au/projects/unsw-nb15-dataset
3. https://www.kaggle.com/datasets/mrwellsdavid/mitm-detection-data
4. https://ton.iotdatasets.com
5. https://www.ll.mit.edu/r-d/datasets

## Setup Instructions
1. 1. Download network traffic datasets with normal + MitM activities
2. 2. Preprocess: extract features (protocol, packet size, flags, time intervals, etc.)
3. 3. Apply machine learning: Isolation Forest, Random Forest, KNN, or Autoencoders
4. 4. Train/test the model on labelled sessions
5. 5. Evaluate results with classification metrics
6. 6. Simulate live attack detection using Scapy or Mininet
7. 7. Visualise flagged connections using Matplotlib or Grafana
8. 8. Optional: Flask dashboard to display detection alerts

## Implementation Guide
1. 1. Confusion matrix showing detection performance
2. 2. Alert system (e.g. console or Flask UI) for flagged MitM sessions
3. 3. Visualisation of network anomaly patterns
4. 4. Model training/evaluation logs
5. 5. Optional network graph for session clustering
6. 6. Performance metrics (accuracy, recall, precision, F1-score)

## Expected Output(s)
1. A functional prototype of an AI-based intrusion detection system that recognises MitM behaviours from network traffic in real time; integration of simulation tools like Wireshark
2. Scapy
3. and ML classifiers

## Background Studies
### Man-in-the-Middle Attacks
Techniques (ARP spoofing, DNS hijack, SSL stripping) and their traffic signatures.

### Network Traffic Analysis
Using packet inspection and flow analysis to understand communication patterns.

### AI in Intrusion Detection
Classification, anomaly detection, and semi-supervised learning in cybersecurity.

### Data Preprocessing
Packet filtering, time-series transformation, feature selection.

### Simulation Tools
Scapy for packet crafting, Mininet for virtual networks.

### Security Metrics
Detection rate, false positive rate, and system latency.

### Real-time Detection Challenges
Managing trade-offs between detection accuracy and system performance.

### Zero-Day Attack Adaptability
Using AI to identify new variants of known attacks.
