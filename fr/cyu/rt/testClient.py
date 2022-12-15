import socket
import time


def sendMessage(host, port, message):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    #message = "1 0 " + str(time.time()) + " 67"
    s.send(message.encode('ascii'))

def runClient():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1', 12345))
    message = "1 0 " + str(time.time()) + " 67"
    print(message)
    s.send(message.encode('ascii'))

    # message received from server
    data = s.recv(1024)
    print('Received from the server :', str(data.decode('ascii')))

    s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s1.connect(('127.0.0.1', 12345))
    message = "6 2 " + str(time.time()) + " 9"

    message = "3 2 " + str(time.time()) + " 789"
    s1.send(message.encode('ascii'))

    # message received from server
    data = s.recv(1024)
    print('Received from the server :', str(data.decode('ascii')))
    s.close()
    s1.close()


    #thread1_client = Client(5006, "192.168.95.22")
    #thread1_client.start()
    #thread2_client = Client("Bonjour", 5006, ct.SERVER_HOST)
    #thread2_client.start()

    # attendre que t1 soit exécuté
    #thread1_client.join()
    # attendre que t2 soit exécuté
    #thread2_client.join()

    print("C'est fini!")

runClient()