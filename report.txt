Network Packet Sniffer with Alert System

1. Introduction
The project implements a real-time packet sniffer with an integrated alert system to monitor traffic and detect malicious patterns like SYN floods, port scans, and ICMP floods.

2. Abstract
This tool uses Python and Scapy to capture packets, analyze patterns, and generate alerts. Alerts are logged in a file and displayed in real time.

3. Tools Used
- Python 3
- Scapy
- Kali Linux

4. Methodology
- Capture live packets using Scapy
- Analyze TCP/UDP/ICMP traffic
- Detect suspicious patterns:
  - SYN Flood (excessive SYN packets)
  - Port Scan (multiple ports from one IP)
  - ICMP Flood (high volume of pings)
- Log results in alerts.log

5. Results
Successfully detected port scans (via Nmap), SYN flood attempts, and ICMP floods. Alerts were stored in logs with timestamps.

6. Conclusion
The sniffer acts as a lightweight IDS. It demonstrates network monitoring, traffic pattern recognition, and security automation. Future improvements could include GUI dashboards, ML-based anomaly detection, and integration with notification systems.
