from fr.cyu.rt.communication import Server
from utils.Constant import Constant as ct


def runServer():
    thread1_server = Server(ct.SERVER_ADRESS, ct.SERVER_PORT_ALARM)
    thread1_server.start()

    #thread1_client = Client("Bonjour", 5006, "192.168.95.22")
    #thread1_client.start()

    #thread2_server = Server(ct.SERVER_ADRESS, SERVER_PORT_NO_ALARM)
    #thread2_server.start()

    # attendre que t1 soit exécuté
    thread1_server.join()
    #thread1_client.join()
    # attendre que t2 soit exécuté
    #thread2_server.join()

runServer()