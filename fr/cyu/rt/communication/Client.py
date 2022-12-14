import socket
import threading


class Client(threading.Thread):
    def __init__(self, message, port, host):
        # calling parent class constructor
        threading.Thread.__init__(self)
        self.message = message
        self.port = port
        self.host = host
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((host, port))
        print('Connexion vers ', host, ':', str(port), ' reussie.')

    def run(self):
        # message = 'Hello word'
        messageFinale = self.message.encode()

        print('Envoi du message', self.message)

        n = self.client.send(messageFinale)

        if (n != len(self.message)):
            print('Erreur envoi.')
        else:
            print('Envoi ok.')

        print('Reception...')
        donnees = self.client.recv(1024)
        print('Recu :', donnees)

        print('Deconnexion.')
        self.client.close()