
from queue import Queue #DS make sure that every port is only scanned once
import socket
import threading #run multiple scanning functions simultaneously.

#https://whatismyipaddress.com/
target = "70.114.161.89"
queue = Queue()
open_ports = []

def portScan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        return False
    
for port in range(1, 1024):
    result = portScan(port)
    if result:
        print("Port {} is open!".format(port))
    else:
        print("port {} is closed!".format(port))
        
def get_ports(mode):
    if mode == 1:
        for port in range(1, 1024):
            queue.put(port)
    elif mode == 2:
        for port in range(1, 49152):
            queue.put(port)
    elif mode == 3:
        ports = [20, 21, 22, 23, 25, 53, 80, 110, 443]
        for port in ports:
            queue.put(port)
    elif mode == 4:
        ports = input("Enter your ports (seperate by blank): ")
        ports = ports.split()
        ports = list(map(int, ports))
        for port in ports:
            queue.put(port)

def worker():
    while not queue.empty():
        port = queue.get()
        if portScan(port):
            print("Port {} is open!").format(port)
            open_ports.append(port)
        else:
            print("Port {} is closed!".format(port))
        
def run_scanner(threads, mode):
    get_ports(mode)
    thread_list = []
    for t in range(threads):
        thread = threading.Thread(target=worker)
    for thread in thread_list:
        thread.start()
    for thread in thread_list:
        thread.join()
    print("open ports are : ", open_ports)
    
run_scanner(100, 1)