import json
import time
from threading import Thread
# websocket.enableTrace(True)
from fr.cyu.rt.communication import ClientWebSocket

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


thread = Thread(target=thread_func)
thread.start()
thread.join()

c.disconnect()

# c.disconnect(lambda d: print("DISCONNECTED"))
