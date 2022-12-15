from business.model.Event import Event
from threading import Thread
from fr.cyu.rt.communication.ClientWebSocket import ClientWebSocket
from fr.cyu.rt.communication.Server import Server
from fr.cyu.rt.communication.Client import Client
from fr.cyu.rt.communication.frame import Frame
from fr.cyu.rt.persistence.mySQLDB.EventPersistence import EventPersistence as ep_mysql
from fr.cyu.rt.persistence.influxDB.EventPersistence import EventPersistence as ep_influx
import time
from fr.cyu.rt.utils.Constant import Constant as ct
import websocket
import logging
import json

TOKEN = "eyJhbGciOiJSUzUxMiJ9.eyJzdWIiOiJjb20iLCJhdXRob3JpdGllcyI6W10sImp0aSI6ImJlODJjZjIzLTE5ZjgtNGI2Zi1iYWUwLTU0ZTkxMTczN2M2YiIsImlhdCI6MTY3MTAwNzQ0MCwiZXhwIjoxNjcxNjEyMjQwfQ.qz6jXaNn4mdUsg15haNAjdTmcCZ51mcfNSmnXu0IMU6JEm7O7v2VWMFUAmkH-_kRvbcQo1oaSvxbjpZwBXKvL79oJ3cG_Rbl9-A9pEt45E6UAmUIFDy8Y9Upa5ch9fBjE7yx2VnBsCRry3rIkuZIOoekOaDeYm9ZzWwIxIbqkHY4WajVlu9mPXIpqQG1qzTOz9sGH8KUFO-WzlzncdWWJ81aBlf4niNMQXwvim1k7H50n3N5FAjGspebli2_toWT9IgvO-rYpyWkQ1KBNshOg-4vFjVuFLSV3sBbwpEmqa5D1iUSTYTiCW318m7EQ6rzpmlr5DAHgcIKK6yT5OxZUdIa3FJ4_joNtdzVrC5G4EKI8MZfeS5trB9-WLzsC2GAqwuAJMtUMsdHncymYooluyuBaiBpbg9udhIOWXffTD5Nnyg0SPr3MH5VbWtUDvnGaRZLKPt1Km6LNqkj2ecX2mhxp7V9Oq1zp11pB9ZzLPs2GB5f4SLESWOsMh4ku5punxZHSiV8VaFKwuszDMdgqp61FCiGoGvsZwr-UBjIzIO1p71fvUWTTF6I4meSe3tpT-poro4unrNoy7BTL807pPf-HSVlvjKsGMhAsq7NWS5FH7jAlLYSAeMqIsW3DHdPsjVQKuAX1_wpsGOiZJEsNpNBnRHmlBnUgN1igni92rs"

c = ClientWebSocket("ws://10.77.46.39:8080/ws")

def on_message(frame) :
    print("RECEIVED MESSAGE")
    print(json.loads(frame.body))


def on_connect(f) :
    print("CONNECTED")


def thread_func() :
    c.connect(headers={"Authorization" : TOKEN}, connectCallback=on_connect, timeout=0)

    c.subscribe("/topic/tests", callback=on_message)
    c.subscribe("/topic/message", callback=on_message)

    while True :
        time.sleep(10)
        print("SEND MESSAGE")
        c.send("/app/test", body=json.dumps({"content" : "COUCOU"}))

'''
thread_socket = Thread(target=thread_func)
thread_socket.start()
thread_socket.join()

c.disconnect()
'''
#thread_server = Server(ct.SERVER_ADRESS, ct.SERVER_PORT_ALARM)
#thread_server.start()
thread_client = Client(ct.PORT_NO_ALARM, ct.HOST_NO_ALARM)
thread_client.start()
thread_client.join()
#thread_server.join()



'''
event = Event(2, 1, time.time(), 0.8989)

ep_influx.insertEvent(event)

results = ep_influx.getEvent()

for r in results:
    print(r)
'''