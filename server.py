# Server program to accept chat messages from clients to JOIN, LIST, MESG, BCST,QUIT
# Sample usage: python3 server.py 8001

#Import libraries
import socket
import sys
import select

# Define the function for creation of a server along with port numbers
def create_server(port):
        svr_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        svr_socket.bind(("0.0.0.0", port))
        svr_socket.listen(1)
        print("Server listening on port: ",port)
        # set socket to unblocking
        svr_socket.setblocking(False)
        connectedSockets=[svr_socket] #sockets for server to monitor (NO MAX)
        clientInfo=[] #usernames of connected clients (MAX 10)

    # Opening a loop for clients to connect. Cliens may leave or connect at any time.
        while True:
                readable,holdOne,holdTwo=select.select(connectedSockets,[],[])

                for currSocket in readable:
                        if currSocket is svr_socket:
                                cli_socket, cli_address = svr_socket.accept() # accept client connection
                                cli_socket.setblocking(False) # set client socket to unblocking too
                                connectedSockets.append(cli_socket)
                        else: #if client already exists in connectedSockets[]
                                try:
                                        data=currSocket.recv(1024)
                                        if data:
                                                response=handleCmd(currSocket,data.decode(),clientInfo)
                                                print("Received msg: ", {data.decode()})
                                                #response= "msg received"
                                                cli_socket.send(response.encode())
                                except BlockingIOError:
                                        continue #call next socket

#        cli_socket.close()
def handleCmd(currSocket, msg,clientInfo):
        inputCmd = msg.split()[0]
        if inputCmd == "JOIN":
                response=("edit join handler")
        elif inputCmd == "LIST":
                response=("edit list handler")
        elif inputCmd == "MESG":
                response=("edit mesg handler")
        elif inputCmd == "BCST":
                response=("edit bcst handler")
        elif inputCmd == "QUIT":
                response=("edit quit handler")
        else:
                response="Unknown Message"

        return response

# The main function
def main():
        if len(sys.argv) != 2: #check arguments
                print("Usage: python3 server.py <svr_port>")
                sys.exit(1)
        port = int(sys.argv[1])

        create_server(port) # start server

# Run script
if __name__ == "__main__":
        main()