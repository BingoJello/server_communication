import socket
import threading
import time

class Client(threading.Thread):
    def __init__(self, port, host):
        # calling parent class constructor
        threading.Thread.__init__(self)
        self.port = port
        self.host = host

    def run(self):

        def sendMessage(message) :
            print('Envoi du message', message)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((self.host, self.port))
            n = s.send(message.encode('ascii'))

            if (n != len(message)) :
                print('Erreur envoi.')
            else :
                print('Envoi ok.')
            s.close()

        #message = "c 1 0" + str(time.time()) + " 67 None"
        message = "1 1 1 "+str(time.time())
        sendMessage(message)
        time.sleep(3)
        #message = "i 1 0" + str(time.time()) + " 98 None"
        message = "0 1 1 " + str(time.time()+1)
        sendMessage(message)