import ping3

#Author :John Peter
#Tool: Ghost finder
print("GHOST FINDER")
print()
print("Discover available hosts in your network with this tool.")
print()
print("Author: John Peter")
print("Any recommendations allowed")

print()
print()

net_mask = str(input("Enter subnet mask(eg '192.168.0.0'): "))
counter = 1
active_hosts = []
print("This might take a while :(")
print("Searching...")
while counter <=255:
    octets = net_mask.split(".")
    last_octet = str(int(octets[-1]) + counter)
    current_ip = ".".join(octets[:-1] + [last_octet])
    response_time = ping3.ping(current_ip)
    if response_time is not False:
        active_hosts.append(current_ip)
        counter += 1
    else:
        counter += 1


for i in active_hosts:
    print(f"{i} is active")

print("Use NMAP to scan for potential vulnerabilities!")
print("For educational purposes only ;)")