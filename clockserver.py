import socket
import datetime
#fn used for initiating clock server
def initateClockServer():
    s = socket.socket()
    print("Socket successfully created")
    #server port
    port = 8000
    s.bind(("",port))
    #start listening to requests
    s.listen(5)
    print("Socket is listening...")
    #clock server running forever
    while True:
        #establish connection with client
        connection, address = s.accept()
        print("Server connected to",address)
        #respond client with server clock time
        connection.send(str(datetime.datetime.now()).encode())
        #close the connection with the client process
        connection.close()
#driver fn
if __name__ == "__main__":
    #trigger the clock server
    initateClockServer()