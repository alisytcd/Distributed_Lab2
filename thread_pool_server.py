import socket
import sys
from threading import Thread
from SocketServer import ThreadingMixIn

data=""
kill=0

class ClientThread(Thread):

    def __init__(self,ip,port):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        print "[+] New server socket thread started for " + ip + ":" + str(port)

    def run(self):
        while True :

            global data
            global TCP_PORT
            global kill
            data = conn.recv(2048)
            if data[:12] == "KILL_SERVICE":
                print "Server received data:", data
                kill=1
                sys.exit
                break
            if data[:4] == "HELO":
                print "Server received data:", data
                MESSAGE = data+"IP:"+str(socket.gethostbyname(socket.gethostname()))+"\nPort:"+str(TCP_PORT)+"\nStudentID:13323690\n"
                conn.send(MESSAGE)

            print "Server received data:", data

# Initialising server
TCP_IP = '0.0.0.0'
TCP_PORT = 8000
BUFFER_SIZE = 20  # Usually 1024, but we need quick response 

tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpServer.bind((TCP_IP, TCP_PORT))
threads = []

#while data[:12]!="KILL_SERVICE" :
while kill!=1:
    tcpServer.listen(4)
    print "Multithreaded Python server : Waiting for connections from TCP clients..."
    (conn, (ip,port)) = tcpServer.accept()
    newthread = ClientThread(ip,port)
    newthread.start()
    threads.append(newthread)

print "out of while loop"
for t in threads:
    t.join()
                                                                                                                          57,1          Bot
