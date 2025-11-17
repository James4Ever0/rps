# intercept request on port 8993 and port 8994.

# we had better put the real server ports other than 8993 and 8994, or use loopback ip address, or flag this request in a special way.

# option 1: onhold the request for 5 seconds and then forward it.
# option 2: drop the request.
# option 3: respond with a custom response.

from scapy.all import *

def packet_callback(packet):
    # print(packet.summary())
    # if packet.haslayer(TCP) and packet[IP].dst == "127.0.0.1":
    #     print("Intercepted request on loopback")
    if packet.haslayer(TCP) and packet[TCP].dport == 8993: # should we spawn a server at this port first?
        print("Intercepted request on port 8993")
    elif packet.haslayer(TCP) and packet[TCP].dport == 8994:
        print("Intercepted request on port 8994")

# cannot sniff on all interfaces.
sniff(prn=packet_callback,iface="lo",filter="tcp",store=0)

# mitm in scapy requires netfilter queue. (nfqueue)