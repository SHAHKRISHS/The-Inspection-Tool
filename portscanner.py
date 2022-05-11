import concurrent.futures
import socket
import threading
import datetime
from termcolor import colored
from main import url


start_time = datetime.datetime.now()

# Threading - We can Perform multiple task simultaneously
print_lock = threading.Lock()
print("\n")
print(colored("Port Scanning Process", 'red'))
print("\n")
# Take input from the user
server = (url)
ip = socket.gethostbyname(server)
print("The ip address of host is", colored(ip, 'green'))

# To print new line
print("\n")

#To print the time when service started.
print("This process will check all the port from 1 to 65,535.\n")
print("The service started at {}".format(start_time.strftime("%c")))
print("\n")

# Pass the ip and port into the function.
def scan_port(ip, port):
    # The socket in the Internet domain, and
    # configures it for stream-oriented communication with default TCP protocol
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    try:
        s.connect((ip, port))
        s.close()
        with print_lock:
            print('Port', colored(port, 'green'), 'and service', colored(socket.getservbyport(port), 'green'),
                  ' is open')
    except:
        pass


with concurrent.futures.ThreadPoolExecutor(max_workers=5000) as executor:
    for port in range(65535):
        executor.submit(scan_port, ip, port + 1)

end_time = datetime.datetime.now()

# To print the time when service ended.
print("\nThe service ended at {}".format(end_time.strftime("%c")))
print("\n")
