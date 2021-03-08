import socket

# PORT SCANNER
# importing socket library with that we are going to make a socket object with default settings# which will get two arguments first argument AF_INET refers to the address family of ipv4 and # second argument SOCK_STREAM refers  connection oriented tcp protocol. 
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# HOST IS OUR TARGET
# Port scanner will scan all of the ports of the target and tell us about those ports which are opened 
print("Enter target IP address or domain name down below")
host=input()
print("Enter number of ports below which you want to scan")
while 0<1:    
    try:
        ports_range=int(input())
        break
    except:
        print("invalid input")
opened_ports_list=[]
for e in range(ports_range):
    dd=(host,e)
    try:
        client.connect(dd)
        opened_ports_list.append(e)
        print("port opened")
    except:
        print("port closed")
print(opened_ports_list)
print("opened ports")


