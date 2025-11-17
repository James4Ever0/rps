import netfilterqueue
import time

packet_list: list[netfilterqueue.Packet] = []

# the processing is sequential
# what is the maximum packet queue size of a single nfqueue?
def detect_and_delay_packet(packet: netfilterqueue.Packet):
    print("Packet detected at:", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    payload = packet.get_payload()
    print("Payload: ", payload)
    packet.retain() # allow later inspection
    # we can choose to not accept the packet here.
    packet_list.append(packet)
    if len(packet_list) > 3:
        time.sleep(5)
        print("Packet delayed for 5 seconds every 3 packets.")
        for p in packet_list:
            p.accept()
        packet_list.clear()

queue = netfilterqueue.NetfilterQueue()
queue.bind(queue_num=2807, user_callback=detect_and_delay_packet,
           max_len=1024, # queue size
           # range=65535, # packet payload size
           )

try:
    queue.run()
finally:
    queue.unbind()