import socket

target = "google.com"
sockt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockt.settimeout(0.5)
ports = []


def port_scan(port_num):
    if sockt.connect_ex((target, port_num)) == 0:
        ports.append(port_num)
    sockt.close()


for x in range(1024):
    port_scan(x)

print(ports)
