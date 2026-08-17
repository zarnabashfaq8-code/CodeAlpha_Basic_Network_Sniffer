from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw
from datetime import datetime

packet_count = 0


def packet_callback(packet):
    global packet_count
    packet_count += 1

    print("\n" + "=" * 70)
    print(f"Packet #{packet_count}")
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    if IP in packet:
        print(f"Source IP       : {packet[IP].src}")
        print(f"Destination IP  : {packet[IP].dst}")

        if TCP in packet:
            print("Protocol        : TCP")
            print(f"Source Port     : {packet[TCP].sport}")
            print(f"Destination Port: {packet[TCP].dport}")

        elif UDP in packet:
            print("Protocol        : UDP")
            print(f"Source Port     : {packet[UDP].sport}")
            print(f"Destination Port: {packet[UDP].dport}")

        elif ICMP in packet:
            print("Protocol        : ICMP")

        else:
            print("Protocol        : Other IP")

        print(f"Packet Length   : {len(packet)} bytes")

        if Raw in packet:
            payload = bytes(packet[Raw].load)
            print(f"Payload         : {payload[:80]!r}")
        else:
            print("Payload         : No application payload")

    else:
        print("Protocol        : Non-IP Packet")
        print(f"Packet Length   : {len(packet)} bytes")


def main():
    print("=" * 70)
    print("                 BASIC NETWORK SNIFFER")
    print("=" * 70)
    print("Capturing network packets...")
    print("Press CTRL+C to stop the sniffer.")
    print("=" * 70)

    try:
        sniff(prn=packet_callback, store=False)

    except KeyboardInterrupt:
        print("\n" + "=" * 70)
        print("              PACKET CAPTURE STOPPED")
        print("=" * 70)
        print(f"Total packets captured: {packet_count}")
        print("=" * 70)

    except PermissionError:
        print("Permission denied. Run the terminal as Administrator.")

    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()