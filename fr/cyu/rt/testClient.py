from communication.Client import Client
from utils.Constant import Constant as ct

def runClient():
    thread1_client = Client("Bonjour", 5006, "192.168.95.22")
    thread1_client.start()
    #thread2_client = Client("Bonjour", 5006, ct.SERVER_HOST)
    #thread2_client.start()

    # attendre que t1 soit exécuté
    #thread1_client.join()
    # attendre que t2 soit exécuté
    #thread2_client.join()

    print("C'est fini!")

runClient()