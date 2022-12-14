import socket
import threading

class Server(threading.Thread):
    def __init__(self, address, port):
        threading.Thread.__init__(self)
        self.address = address
        self.port = port
        self.serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serveur.bind((address, port))
        self.serveur.listen(1)


    def run(self):
        while (True):
            client, addressClient = self.serveur.accept()
            print('Connexion de ', addressClient)

            data = client.recv(1024)

            if not data:
                print('Erreur de reception.')
            else:
                print('Reception de:', data, ' sur le port', self.port)

                response = data.upper()
                print('Envoi de :', response)
                n = client.send(response)
                if (n != len(response)):
                    print('Erreur envoi.')
                else:
                    print('Envoi ok.')