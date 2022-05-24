import socket
from IPy import IP

def scan(target):
    converted_ip = check_ip(target)
    print("\n" + "[-_0 Scanning Target] " + str(target))
    for port in range(1, 65535):
        scan_port(converted_ip, port)

def check_ip(ip):
    try:
        IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)

def get_banner(s):
    return s.recv(1024)

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ipaddress, port))
        try:
            banner = get_banner(sock)
            print("[+] Open Port {0} : {1}" .format(port,banner.decode().strip("\n")))
            f = open("banners.txt", "a")
            f.writelines(banner.decode().strip("\n").strip("\r"))
        except:
            print("[+] Open Port {}".format(port))
    except:
        pass

if __name__ == "__main__":
    targets = input("[+] Enter Target/s To Scan(split multiple targets with ,): ")
    if "," in targets:
        for ip_add in targets.split(","):
            scan(ip_add.strip(" "))
    else:
        scan(targets)
