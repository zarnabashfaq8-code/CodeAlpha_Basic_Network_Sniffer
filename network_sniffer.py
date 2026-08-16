from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw
from datetime import datetime

MAX_PACKETS = 30
packet_count = 0


def packet_callback(packet):
    global packet_count

    packet_count += 1

    print("\n" + "=" * 70)
    print(f"Packet #{packet_count}")
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # Check for IP layer
    if IP in packet:

        source_ip = packet[IP].src
        destination_ip = packet[IP].dst

        print(f"Source IP       : {source_ip}")
        print(f"Destination IP  : {destination_ip}")

        # TCP
        if TCP in packet:
            print("Protocol        : TCP")
            print(f"Source Port     : {packet[TCP].sport}")
            print(f"Destination Port: {packet[TCP].dport}")

        # UDP
        elif UDP in packet:
            print("Protocol        : UDP")
            print(f"Source Port     : {packet[UDP].sport}")
            print(f"Destination Port: {packet[UDP].dport}")

        # ICMP
        elif ICMP in packet:
            print("Protocol        : ICMP")

        else:
            print("Protocol        : Other IP Protocol")

        print(f"Packet Length   : {len(packet)} bytes")

        # Display limited payload information
        if Raw in packet:
            payload = bytes(packet[Raw].load)

            try:
                readable_payload = payload[:80].decode(
                    "utf-8",
                    errors="replace"
                )

                print(f"Payload         : {readable_payload}")

            except Exception:
                print("Payload         : Binary/Non-readable data")

        else:
            print("Payload         : No application payload")

    else:
        print("Protocol        : Non-IP Packet")
        print(f"Packet Length   : {len(packet)} bytes")


def main():

    print("=" * 70)
    print("             BASIC NETWORK SNIFFER")
    print("=" * 70)
    print(f"Capturing maximum {MAX_PACKETS} packets...")
    print("=" * 70)

    try:

        sniff(
            prn=packet_callback,
            count=MAX_PACKETS,
            store=False
        )

        print("\n" + "=" * 70)
        print("Packet capture completed.")
        print(f"Total packets captured: {packet_count}")
        print("=" * 70)

    except PermissionError:

        print("\nPermission denied.")
        print("Please run Command Prompt as Administrator.")

    except Exception as error:

        print("\nAn error occurred:")
        print(error)


if __name__ == "__main__":
    main()