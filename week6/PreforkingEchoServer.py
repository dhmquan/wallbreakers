import socket
import sys
import os

#set up the socket
listener = socket.socket()
listener.bind(('localhost', 8282))
listener.listen()

n = 3
if len(sys.argv) > 1:
    n = int(sys.argv[1])

#begin forking
for i in range(n):
    pid = os.fork()

    if pid == 0:
        childpid = os.getpid()
        print("Child %s listening" % childpid)
        try:
            while 1:
                conn, addr = listener.accept()
                
                reader = conn.makefile()
                message = reader.readline()

                writer = conn.makefile('w')
                writer.write('Child %s echo: %s' % (childpid, message))
                writer.flush()

                conn.close()
                print("Child %s echo: %s" % (childpid, message))

        except KeyboardInterrupt:
            sys.exit()

try:
    os.waitpid(-1, 0)

except KeyboardInterrupt:
    sys.exit()