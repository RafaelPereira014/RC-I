import socket
import signal
import sys
import psutil

def signal_handler(sig, frame):
    print('\nDone!')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

ip_addr = "127.0.0.1"
tcp_port = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((ip_addr, tcp_port))

while True:
    try: 
       
        cpu = psutil.cpu_percent(4)
        print('My CPU usage is: ',cpu)
        cpu_usage = bytes(str(cpu),encoding="UTF-8")
        sock.send(cpu_usage)
        
        memory = psutil.virtual_memory().percent
        print('My memory percentage is: ',memory)
        memory_percentage = bytes(str(memory),encoding="UTF-8")
        sock.send(memory_percentage)
        
    except (socket.timeout, socket.error):
        print('Server error. Done!')
        sys.exit(0)
