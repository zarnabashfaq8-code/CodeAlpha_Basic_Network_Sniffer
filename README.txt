............
Requirements
............

Python 3.x
Scapy
Npcap (required on Windows for packet capturing)


............
Installation
............

Install the required Python library using:

pip install -r requirements.txt

On Windows, Npcap is required for packet capture.


...........
How to Run
...........

Open the project directory in Command Prompt or PowerShell and run:

python network_sniffer.py

The program will start capturing network packets continuously.

Press CTRL+C to stop the packet capture.

After stopping, the program will display the total number of packets captured.


Sample Output

======================================================================
             BASIC NETWORK SNIFFER
======================================================================
Capturing network packets...
Press CTRL+C to stop the sniffer.
======================================================================

======================================================================
Packet #1
Time: 2026-08-16 20:05:21
Source IP       : 192.168.1.5
Destination IP  : 142.250.xxx.xxx
Protocol        : TCP
Source Port     : 52341
Destination Port: 443
Packet Length   : 66 bytes
Payload         : No application payload
======================================================================

Packet capture stopped.
Total packets captured: 47
======================================================================


.................
Learning Outcomes
.................

Through this project, I learned:

The basic structure of network packets.
How source and destination IP addresses identify communicating endpoints.
The differences between TCP, UDP, and ICMP traffic.
How ports are used by network applications.
How Python and Scapy can be used for basic packet capture and analysis.
The importance of monitoring and understanding network traffic in cybersecurity.


......................
Ethical Considerations
......................

This network sniffer is developed for educational and authorized network analysis purposes only. Packet capture should only be performed on systems and networks where the user has permission to monitor traffic.

The project should not be used to intercept or monitor network traffic without proper authorization.


..........
Conclusion
..........

This project provides a practical introduction to network packet capturing and analysis. It demonstrates how Python and Scapy can be used to inspect basic network traffic and understand communication through different protocols.

The project helped develop practical knowledge of packet structure, IP addresses, ports, and network protocols, which are important concepts in cybersecurity and network security.