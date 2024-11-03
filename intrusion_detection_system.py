
import socket
import os
import struct
import time
from collections import defaultdict

SYN_THRESHOLD = 20
syn_count = defaultdict(int)

def block_ip(ip):
    print(f"Bloqueando o IP: {ip}")
    os.system(f"iptables -A INPUT -s {ip} -j DROP")

def detect_syn_flood():
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
    
    while True:
        packet, addr = s.recvfrom(65535)
        src_ip = addr[0]
        
        ip_header = packet[0:20]
        iph = struct.unpack('!BBHHHBBH4s4s', ip_header)
        
        tcp_header = packet[20:40]
        tcph = struct.unpack('!HHLLBBHHH', tcp_header)
        
        tcp_flags = tcph[5]
        syn_flag = tcp_flags & 0x02
        
        if syn_flag:
            syn_count[src_ip] += 1
            print(f"Pacote SYN recebido de {src_ip}. Contagem atual: {syn_count[src_ip]}")
            
            if syn_count[src_ip] > SYN_THRESHOLD:
                block_ip(src_ip)
                with open("log.txt", "a") as log_file:
                    log_file.write(f"{time.ctime()}: Bloqueio do IP {src_ip} por ataque SYN flood\n")
                syn_count[src_ip] = 0
            
        time.sleep(1)
        syn_count.clear()

if __name__ == "__main__":
    print("Iniciando o IDS para detectar SYN flood...")
    detect_syn_flood()
