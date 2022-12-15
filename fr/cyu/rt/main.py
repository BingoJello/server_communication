from business.model.Event import Event
from threading import Thread

from fr.cyu.rt.business.model.EventType import EventType
from fr.cyu.rt.communication.ClientWebSocket import ClientWebSocket
from fr.cyu.rt.communication.Server import Server
from fr.cyu.rt.communication.Client import Client
from fr.cyu.rt.communication.frame import Frame
from fr.cyu.rt.persistence.mySQLDB.EventPersistence import EventPersistence as ep_mysql
from fr.cyu.rt.persistence.influxDB.EventPersistence import EventPersistence as ep_influx
import time
from fr.cyu.rt.utils.Constant import Constant as ct



thread_server = Server(ct.SERVER_ADRESS, ct.SERVER_PORT_ALARM)
thread_server.start()
thread_server.join()
''''
thread_client = Client(ct.PORT_NO_ALARM, ct.HOST_NO_ALARM)
thread_client.start()
thread_client.join()

['i', '1', '0', '1671119630.8397105', 'None']
'''

