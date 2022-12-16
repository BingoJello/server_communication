import socket
import threading
import time
import websocket
import logging
import json
from datetime import datetime
from fr.cyu.rt.business.model.Event import Event
from fr.cyu.rt.persistence.mySQLDB.EventPersistence import EventPersistence as mysql_persist
from fr.cyu.rt.business.model.EventType import EventType
from fr.cyu.rt.communication.ClientWebSocket import ClientWebSocket

class Client(threading.Thread):
    def __init__(self, port, host):
        # calling parent class constructor
        threading.Thread.__init__(self)
        self.port = port
        self.host = host
        self.token = "eyJhbGciOiJSUzUxMiJ9.eyJzdWIiOiJjb20iLCJhdXRob3JpdGllcyI6W10sImp0aSI6ImJlODJjZjIzLTE5ZjgtNGI2Zi1iYWUwLTU0ZTkxMTczN2M2YiIsImlhdCI6MTY3MTAwNzQ0MCwiZXhwIjoxNjcxNjEyMjQwfQ.qz6jXaNn4mdUsg15haNAjdTmcCZ51mcfNSmnXu0IMU6JEm7O7v2VWMFUAmkH-_kRvbcQo1oaSvxbjpZwBXKvL79oJ3cG_Rbl9-A9pEt45E6UAmUIFDy8Y9Upa5ch9fBjE7yx2VnBsCRry3rIkuZIOoekOaDeYm9ZzWwIxIbqkHY4WajVlu9mPXIpqQG1qzTOz9sGH8KUFO-WzlzncdWWJ81aBlf4niNMQXwvim1k7H50n3N5FAjGspebli2_toWT9IgvO-rYpyWkQ1KBNshOg-4vFjVuFLSV3sBbwpEmqa5D1iUSTYTiCW318m7EQ6rzpmlr5DAHgcIKK6yT5OxZUdIa3FJ4_joNtdzVrC5G4EKI8MZfeS5trB9-WLzsC2GAqwuAJMtUMsdHncymYooluyuBaiBpbg9udhIOWXffTD5Nnyg0SPr3MH5VbWtUDvnGaRZLKPt1Km6LNqkj2ecX2mhxp7V9Oq1zp11pB9ZzLPs2GB5f4SLESWOsMh4ku5punxZHSiV8VaFKwuszDMdgqp61FCiGoGvsZwr-UBjIzIO1p71fvUWTTF6I4meSe3tpT-poro4unrNoy7BTL807pPf-HSVlvjKsGMhAsq7NWS5FH7jAlLYSAeMqIsW3DHdPsjVQKuAX1_wpsGOiZJEsNpNBnRHmlBnUgN1igni92rs"
        self.list_send_rasb = ['USER_CONTROL', 'USER_CONTROL_END', 'USER_ACTIVATION', 'USER_DEACTIVATION']

        while True:
            try:
                self.c = ClientWebSocket("ws://10.77.46.39:8080/ws")
                break
            except:
                logging.log("web socket error - reconnecting")
                time.sleep(5)

    def run(self):
        def sendMessage(message) :
            print('Envoi du message', message)
            while True:
                try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.connect((self.host, self.port))
                    print('Envoi du message OK')
                    break
                except :
                    print("socket error {} reconnecting")
                    time.sleep(5)
            while True:
                try:
                    s.send(message.encode('ascii'))
                    s.close()
                    break
                except:
                    print("socket error {} resending message")
                    time.sleep(5)


        def on_message_camera(frame):
            event_json = json.loads(frame.body)
            angle_x = str(event_json['angleX'])
            angle_y = str(event_json['angleY'])
            message = '1 ' + angle_x + ' ' + angle_y + ' ' + str(time.time())
            print('envoie camera')
            print(message)
            sendMessage(message)

        def on_message_event(frame):
            event_json = json.loads(frame.body)
            eventTypeID = EventType[event_json['eventType']].value
            eventTypeLabel = EventType[event_json['eventType']].name

            if event_json['value'] != '' :
                value = event_json['value']
            else :
                value = 'None'

            dateTime = datetime.fromisoformat(event_json['timestamp'])
            timestamp = dateTime.timestamp()
            event = Event(eventTypeID, -1, timestamp, value)
            mysql_persist.insertEvent(event)

            if eventTypeLabel in self.list_send_rasb:
                message = eventTypeID + ' 0 0 ' + timestamp
                print('envoie event')
                print(message)
                sendMessage(message)

        def on_connect(f) :
            print("CONNECTED")

        def on_error(f):
            print("web socket error- reconnecting")
            time.sleep(5)

        while True:
            try:
                self.c.connect(headers={"Authorization" : self.token}, errorCallback=on_error, connectCallback=on_connect, timeout=0)
                self.c.subscribe("/topic/house/camera", callback=on_message_camera)
                self.c.subscribe("/topic/house/event", callback=on_message_event)
                break
            except:
                print("web socket error {} reconnecting")
                time.sleep(5)

        '''
        #message = "c 1 0" + str(time.time()) + " 67 None"
        message = "1 1 1 "+str(time.time())
        sendMessage(message)
        time.sleep(3)
        #message = "i 1 0" + str(time.time()) + " 98 None"
        message = "0 1 1 " + str(time.time()+1)
        sendMessage(message)
        '''