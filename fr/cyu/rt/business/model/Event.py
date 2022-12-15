import time
from datetime import datetime
from fr.cyu.rt.business.model.SensorType import SensorType
from fr.cyu.rt.business.model.EventType import EventType


class Event:
    def __init__(self):
        self.eventTypeID = -1
        self.eventTypeLabel = EventType(-1).name
        self.sensorTypeID = -1
        self.sensorTypeLabel = SensorType(-1).name
        self.timestamp = time.time()
        self.dateTime = datetime.now()
        self.measurement = None
        self.img = None

    def __init__(self, eventTypeID=-1, sensorTypeID=-1, timestamp=time.time(), measure=None, img=None):
        if int(eventTypeID) in EventType._value2member_map_.keys():
            self.eventTypeID = int(eventTypeID)
            self.eventTypeLabel = EventType(int(eventTypeID)).name
        else:
            self.eventTypeID = -1
            self.eventTypeLabel = EventType(-1).name

        if int(sensorTypeID) in SensorType._value2member_map_.keys() :
            self.sensorTypeID = int(sensorTypeID)
            self.sensorTypeLabel = SensorType(int(sensorTypeID)).name
        else :
            self.sensorTypeID = -1
            self.sensorTypeLabel = SensorType(-1).name

        self.timestamp = float(timestamp)
        self.dateTime = datetime.fromtimestamp(float(timestamp))
        if measure is not None:
            self.measure = float(measure)
        self.img = img

    def getEventTypeID(self):
        return self.eventTypeID

    def setEventTypeID(self, eventTypeID):
        if eventTypeID in EventType._value2member_map_.keys() :
            self.eventTypeID = eventTypeID
        else :
            self.eventTypeID = 0

    def getEventTypeLabel(self):
        return self.eventTypeLabel

    def setEventTypeLabel(self, eventTypeLabel):
        try :
            self.eventTypeLabel = EventType[eventTypeLabel]
        except :
            self.eventTypeLabel = 'NONE'

    def getSensorTypeID(self) :
        return self.sensorTypeID

    def setSensorTypeID(self, sensorTypeID) :
        if sensorTypeID in SensorType._value2member_map_.keys() :
            self.sensorTypeID = sensorTypeID
        else :
            self.sensorTypeID = 0

    def getSensorTypeLabel(self) :
        return self.sensorTypeLabel

    def setSensorTypeLabel(self, sensorTypeLabel) :
        try :
            self.sensorTypeLabel = SensorType[sensorTypeLabel]
        except :
            self.sensorTypeLabel = 'NONE'

    def getTimestamp(self):
        return self.timestamp

    def setTimestamp(self, timestamp):
        self.timestamp = timestamp

    def getDateTime(self):
        return self.dateTime

    def setDateTime(self, timestamp):
        self.timestamp = timestamp
        self.dateTime = datetime.fromtimestamp(timestamp)

    def getMeasure(self):
        return self.measure

    def setMeasure(self, measure):
        self.measure = measure

    def getImg(self):
        return self.img

    def setImg(self, img):
        self.img = img

    def __str__(self) :
        return f'{self.eventTypeID} {self.eventTypeLabel} {self.sensorTypeID} {self.sensorTypeLabel} ' \
               f'{self.dateTime} {self.measure} {self.img}'