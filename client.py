# Client program to connect to server, create username, and send messages
# Sample usage: python3 client.py ecs-coding3.csus.edu  8000
#Import libraries
import socket
import sys
import select

# Define the function for creation of a client
def create_client(svr_ip, svr_port):
    cli_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cli_socket.connect((svr_ip, svr_port))
    
    cli_socket.setblocking(False)
    #begin communication with the server
    print("Enter JOIN followed by your username: ")
    while True:
        read,_,_ = select.select([sys.stdin, cli_socket],[],[])
        #Read through all select ports to see if there is incoming keyboard input or messages
        for word in read:
            if word is sys.stdin:
                #accept user input
                message = input()
                cli_socket.send(message.encode())
            elif word is cli_socket:
                #accept server data
                try:
                    response = cli_socket.recv(1024)
                    if response:
                        print(f"{response.decode()}")
                except BlockingIOError:
                    pass
                    #error handling

    cli_socket.close()

# Define the main function
def main():
    if len(sys.argv) != 3: #check for valid arguments
        print("Usage: python3 client.py <server_ip> <server_port>")
        sys.exit(1)
    # Separate the strings of IP address and Port informartion
    svr_ip =sys.argv[1]
    svr_port = int(sys.argv[2])

    create_client(svr_ip, svr_port)

# Run script
if __name__ == "__main__":
    main()