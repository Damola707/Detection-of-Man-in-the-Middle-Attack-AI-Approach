# Detection of Man-in-the-Middle Attack: AI Approach

##  Introduction
This project focuses on detecting **Man-in-the-Middle (MITM) attacks** using artificial intelligence. It analyzes network traffic data and classifies whether the connection is normal or malicious based on key traffic patterns.

---

##  Background Studies

###  Man-in-the-Middle Attacks
Covers ARP spoofing, DNS hijacking, and SSL stripping. These techniques involve intercepting communication between two parties. Each method has distinct traffic signatures that can be detected through inspection.

###  Network Traffic Analysis
Involves inspecting packets and analyzing flow data to understand normal vs. malicious communication behaviors.

###  AI in Intrusion Detection
AI enables classification of traffic and anomaly detection. It helps in identifying known and unknown (zero-day) threats. Both supervised and semi-supervised learning approaches are useful in cybersecurity.

###  Data Preprocessing
This includes:
- Packet filtering (removing irrelevant records),
- Feature selection (choosing the most useful columns),
- Standardization (scaling data using tools like StandardScaler).

###  Simulation Tools (Optional in this version)
- **Scapy**: Used for crafting or injecting packets.
- **Mininet**: Used to simulate virtual networks for testing.

###  Security Metrics
Used to evaluate the model:
- Detection Rate
- False Positive Rate
- System Latency

###  Real-Time Detection Challenges
Striking a balance between detection accuracy and system performance (speed) is key in real-time systems.

###  Zero-Day Attack Adaptability
AI models should generalize well enough to detect variations of known attacks — critical for evolving MITM tactics.

---

##  Dataset
The model is trained on the **UNSW-NB15 dataset**, which contains labeled records of normal and attack traffic. It provides a solid foundation for intrusion detection research.

---

##  Model Training
- **Library Used**: `scikit-learn`
- **Algorithm**: Decision Tree Classifier
- **Scaler**: StandardScaler (for normalization)
- **Output Files**:
  - `model.pkl`: Trained decision tree model
  - `scaler.pkl`: Saved normalization scaler

---

##  Evaluation
Performance was measured using:
- **Detection Rate**
- **False Positive Rate**

These metrics help determine how effective the model is at identifying attacks vs. falsely flagging safe traffic.

---

##  Running the Project

### 1. Install dependencies
```bash
pip install pandas scikit-learn
