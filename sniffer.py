from scapy.all import sniff, TCP, IP, ICMP
from collections import defaultdict
import time

# Track packet counts
syn_count = defaultdict(int)
icmp_count = defaultdict(int)
port_scan_tracker = defaultdict(set)

LOG_FILE = "alerts.log"

def log_alert(message):
    print(message)
    with open(LOG_FILE, "a") as f:
        f.write(f"{time.ctime()} - {message}\n")

def analyze_packet(packet):
    if packet.haslayer(IP):
        src_ip = packet[IP].src

        # Detect SYN Flood
        if packet.haslayer(TCP) and packet[TCP].flags == "S":
            syn_count[src_ip] += 1
            if syn_count[src_ip] > 100:
                log_alert(f"[ALERT] Possible SYN Flood from {src_ip}")

            # Track unique ports for Port Scan detection
            dport = packet[TCP].dport
            port_scan_tracker[src_ip].add(dport)
            if len(port_scan_tracker[src_ip]) > 10:
                log_alert(f"[ALERT] Possible Port Scan from {src_ip} on ports {list(port_scan_tracker[src_ip])}")

        # Detect ICMP Flood
        if packet.haslayer(ICMP):
            icmp_count[src_ip] += 1
            if icmp_count[src_ip] > 50:
                log_alert(f"[ALERT] Possible ICMP Flood from {src_ip}")

def main():
    print("🚨 Starting Packet Sniffer with Alert System... (Press Ctrl+C to stop)")
    sniff(prn=analyze_packet, store=0)

if __name__ == "__main__":
    main()
