import socket

# Take server name
host = input("Enter website address: ")


try:
    # To know IP Address of any website
    addr = socket.gethostbyname(host)
    print("IP Address of website ", addr)
    print("Host Address of website ", socket.gethostbyaddr(host))
    print("Host HostName ex of website ", socket.gethostbyname_ex(host))
    print("Host Name of website ", socket.gethostname())
except socket.gaierror:
    print("Website does not exist")