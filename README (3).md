# 🚨 Network Packet Sniffer with Alert System

## 🎯 Objective
A Python-based real-time packet sniffer that captures and analyzes network traffic using **Scapy** and generates alerts for suspicious activities such as **Port Scans**, **SYN Floods**, and **ICMP Floods**.

---

## 🛠 Tools & Technologies
- Python 3
- Scapy library
- SQLite (optional for logging)
- Kali Linux / Ubuntu / Windows with Scapy

---

## 🧪 Features
- Captures live packets from the network interface
- Detects suspicious activities:
  - Multiple SYN packets → **Possible SYN Flood**
  - Sequential connections to multiple ports → **Possible Port Scan**
  - Excessive ICMP echo requests → **Possible ICMP Flood**
- Logs alerts with timestamp in `alerts.log`
- Displays real-time warnings in the terminal

---

## 📦 Installation
```bash
git clone https://github.com/mcranjit/network-packet-sniffer.git
cd network-packet-sniffer
pip install -r requirements.txt
```

---

## ▶️ Usage
Run the sniffer (requires root/admin privileges):
```bash
sudo python3 sniffer.py
```

---

## 📊 Output Example
```
[ALERT] Possible Port Scan detected from 192.168.1.15 on ports 22, 80, 443
[ALERT] SYN Flood suspected from 10.0.0.5 - 200 SYN packets in 10 seconds
```

Alerts are also saved in **alerts.log**.

---

## ✅ Outcome
This project demonstrates how to build a basic **Intrusion Detection System (IDS)** using Python and Scapy, showcasing skills in network monitoring, traffic analysis, and security automation.

---
