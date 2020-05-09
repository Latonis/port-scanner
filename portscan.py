import socket

target = "localhost"
targetIP = socket.gethostbyname(target)
ports = []


def port_scan(port_num):
    sockt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sockt.settimeout(0.1)
    if sockt.connect_ex((target, port_num)) == 0:
        ports.append(port_num)
    sockt.close()


for x in range(1,1024):
    port_scan(x)

for port in ports:
    print("Port {}: OPEN".format(port))
