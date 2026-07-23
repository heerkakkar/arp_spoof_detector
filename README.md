# ARP Spoofing Detector

A simple Python-based ARP Spoofing Detector built using **Scapy**. This project monitors live ARP packets on a local network, learns IP-to-MAC address mappings, and alerts when the same IP address is associated with a different MAC address, which may indicate an ARP spoofing attack.

---

## Features

- Capture live network packets using Scapy
- Filter and analyze only ARP packets
- Learn and store IP → MAC mappings
- Detect changes in MAC addresses for the same IP
- Display a warning for possible ARP spoofing attacks
- Beginner-friendly and easy to understand

---

## Technologies Used

- Python 3
- Scapy
- Networking Concepts
  - ARP
  - IP Addressing
  - MAC Addresses
  - Packet Sniffing

---

## Project Structure

```
arp_spoof_detector/
│
├── main.py              # Starts packet sniffing
├── detector.py          # ARP detection logic
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/arp_spoof_detector.git
```

Move into the project directory:

```bash
cd arp_spoof_detector
```

Install the required package:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the detector:

```bash
python main.py
```

The program continuously listens for ARP packets and compares IP-to-MAC mappings. If an IP address is seen with a different MAC address than before, a warning is displayed.

---

## How It Works

1. Capture live packets using Scapy.
2. Filter only ARP packets.
3. Extract the sender's IP and MAC address.
4. Store the IP → MAC mapping.
5. Compare future ARP packets against stored mappings.
6. Display an alert if the same IP is associated with a different MAC address.

---

## Example Output

```
New Device
IP : 192.168.1.1
MAC: AA:BB:CC:DD:EE:FF
----------------------------------------

Possible ARP Spoofing Detected!

IP : 192.168.1.1
Old MAC : AA:BB:CC:DD:EE:FF
New MAC : 11:22:33:44:55:66
```

---

## Limitations

This project demonstrates the basic principle behind ARP spoofing detection. It may generate false positives in situations where legitimate MAC address changes occur, such as network hardware replacement or certain network reconfigurations.

---

## What I Learned

While building this project, I learned:

- Python programming
- Dictionaries and functions
- Working with Python modules
- Packet sniffing using Scapy
- Ethernet and ARP protocols
- IP and MAC addressing
- Basic network security concepts
- ARP spoofing detection logic

---

## Future Improvements

- Save alerts to a log file
- Colored terminal output
- Command-line interface for selecting network interfaces
- Graphical user interface (GUI)
- Email or desktop notifications
- Improved verification to reduce false positives

---

## License

This project is intended for educational purposes.