from scapy.all import ARP

arp_table = {}

def process_packet(packet):

    if packet.haslayer(ARP):

        sender_ip = packet[ARP].psrc
        sender_mac = packet[ARP].hwsrc

        if sender_ip not in arp_table:

            arp_table[sender_ip] = sender_mac
            print(f"New Device")
            print(f"IP : {sender_ip}")
            print(f"MAC: {sender_mac}")
            print("-"*40)

        else:

            if arp_table[sender_ip] != sender_mac:

                print("\nPossible ARP Spoofing Detected!")

                print(f"IP : {sender_ip}")
                print(f"Old MAC : {arp_table[sender_ip]}")
                print(f"New MAC : {sender_mac}")