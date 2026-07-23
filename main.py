from scapy.all import sniff
from detector import process_packet

print("ARP Spoofing Detector Started...")

sniff(
    prn=process_packet,
    store=False
)