import socket
import threading
import sys
import time
import websocket
import logging
import json
from fr.cyu.rt.communication.ClientWebSocket import ClientWebSocket
from fr.cyu.rt.business.model.Event import Event
from fr.cyu.rt.persistence.influxDB.EventPersistence import EventPersistence as influx_persist
from fr.cyu.rt.persistence.mySQLDB.EventPersistence import EventPersistence as mysql_persist
from datetime import datetime

class Server(threading.Thread):
    def __init__(self, address, port):
        threading.Thread.__init__(self)
        self.address = address
        self.port = port
        while True:
            try:
                self.serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.serveur.bind((address, port))
                self.serveur.listen(1)
                break
            except:
                time.sleep(2)
                print('Tentative de connexion avec le socket echoué - Reconnection')

        self.token = "eyJhbGciOiJSUzUxMiJ9.eyJzdWIiOiJjb20iLCJhdXRob3JpdGllcyI6W10sImp0aSI6ImJlODJjZjIzLTE5ZjgtNGI2Zi1iYWUwLTU0ZTkxMTczN2M2YiIsImlhdCI6MTY3MTAwNzQ0MCwiZXhwIjoxNjcxNjEyMjQwfQ.qz6jXaNn4mdUsg15haNAjdTmcCZ51mcfNSmnXu0IMU6JEm7O7v2VWMFUAmkH-_kRvbcQo1oaSvxbjpZwBXKvL79oJ3cG_Rbl9-A9pEt45E6UAmUIFDy8Y9Upa5ch9fBjE7yx2VnBsCRry3rIkuZIOoekOaDeYm9ZzWwIxIbqkHY4WajVlu9mPXIpqQG1qzTOz9sGH8KUFO-WzlzncdWWJ81aBlf4niNMQXwvim1k7H50n3N5FAjGspebli2_toWT9IgvO-rYpyWkQ1KBNshOg-4vFjVuFLSV3sBbwpEmqa5D1iUSTYTiCW318m7EQ6rzpmlr5DAHgcIKK6yT5OxZUdIa3FJ4_joNtdzVrC5G4EKI8MZfeS5trB9-WLzsC2GAqwuAJMtUMsdHncymYooluyuBaiBpbg9udhIOWXffTD5Nnyg0SPr3MH5VbWtUDvnGaRZLKPt1Km6LNqkj2ecX2mhxp7V9Oq1zp11pB9ZzLPs2GB5f4SLESWOsMh4ku5punxZHSiV8VaFKwuszDMdgqp61FCiGoGvsZwr-UBjIzIO1p71fvUWTTF6I4meSe3tpT-poro4unrNoy7BTL807pPf-HSVlvjKsGMhAsq7NWS5FH7jAlLYSAeMqIsW3DHdPsjVQKuAX1_wpsGOiZJEsNpNBnRHmlBnUgN1igni92rs"

        while True:
            try:
                self.c = ClientWebSocket("ws://10.77.46.39:8080/ws")
                break
            except:
                print('Erreur de connection au web socket - Reconnection')
                time.sleep(2)

        self.queue = []

    def run(self):
        def on_message(frame) :
            print("RECEIVED MESSAGE")
            print(json.loads(frame.body))

        def on_connect(f) :
            print("CONNECTED")

        def on_error(f) :
            print("web socket error- reconnecting")
            time.sleep(5)

        while True:
            try:
                self.c.connect(headers={"Authorization" : self.token}, errorCallback=on_error, connectCallback=on_connect, timeout=0)
                #self.c.subscribe("/topic/tests", callback=on_message)
                #self.c.subscribe("/topic/message", callback=on_message)
                break
            except:
                print("socket error reconnecting")
                time.sleep(5)

        while True:
            try :
                client, addressClient = self.serveur.accept()
                print('Connexion de ', addressClient)

                data = client.recv(350000)

                if not data:
                    print('Erreur de reception du rasberry')
                    continue
                else:
                    print('Reception de:', data, ' sur le port', self.port)
                    list_elt = data.decode("utf-8").split(' ', 4)

                    if len(list_elt) == 5:
                        if list_elt[0] == 'p':
                            if len(self.queue) >= 3:
                                self.queue.pop(2)
                            self.queue.append([list_elt[3], list_elt[4]])
                            print('image')
                            print(len(list_elt[4]))
                            event_dict = {'content': list_elt[4]}
                            try:
                                self.c.send("/app/house/camera", body=json.dumps(event_dict))
                            except:
                                continue
                            continue
                        elif list_elt[0] == 'i' :
                            list_elt[0] = 4
                        else:
                            list_elt[0] = 8

                        event = Event(list_elt[0], list_elt[1], list_elt[3], list_elt[2], list_elt[4])
                        print('Sensor')
                        print(event)
                        event_dict = {'sensorId' : str(event.getSensorTypeID()),
                                      'sensorType' : event.getSensorTypeLabel(),
                                      'value' : str(event.getMeasure()),
                                      'timestamp' : datetime.now().isoformat()}

                        try:
                            self.c.send("/app/house/sensor", body=json.dumps(event_dict))
                        except:
                            continue

                        if list_elt[0] == 4:
                            event = Event(list_elt[0], list_elt[1], list_elt[3], list_elt[2], list_elt[4])

                            event_dict = {'alertType':'ALERT',
                                          'sensorId' : str(event.getSensorTypeID()),
                                          'sensorType' : event.getSensorTypeLabel(),
                                          'value': str(event.getMeasure()),
                                          'timestamp' : datetime.now().isoformat()}
                            print("Alerte")
                            mysql_persist.insertEvent(event)

                            for pic in self.queue:
                                event_pic = Event(11, 0, pic[0], 0, pic[1])
                                mysql_persist.insertEvent(event_pic)
                            try:
                                self.c.send("/app/house/alert", body=json.dumps(event_dict))
                            except:
                                continue
                        else:
                            list_elt[0] = 8
                            event = Event(list_elt[0], list_elt[1], list_elt[3], list_elt[2], list_elt[4])
                            print(event)
                            influx_persist.insertEvent(event)

            except:
                while True:
                    print("socket error reconnecting")
                    time.sleep(5)
                    try :
                        self.serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        self.serveur.bind((self.address, self.port))
                        self.serveur.listen(1)
                        break
                    except :
                        print("socket error - reconnecting")
                        time.sleep(5)