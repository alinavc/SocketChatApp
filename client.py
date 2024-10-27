# Client program to connect to server, create username, and send messages
# Sample usage: python3 client.py ecs-coding3.csus.edu  8000
#Import libraries
import socket
import sys

# Define the function for creation of a client
def create_client(svr_ip, svr_port):
    cli_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cli_socket.connect((svr_ip, svr_port))

    # Communicate with the server
    message = input("Awaiting Command: ")
    cli_socket.send(message.encode())

    response = cli_socket.recv(1024)
    if response:
        print(f"Received from server: {response.decode()}")
   # cli_socket.close()

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
