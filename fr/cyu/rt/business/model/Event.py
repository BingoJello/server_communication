import time
from datetime import datetime
from fr.cyu.rt.business.model.SensorType import SensorType
from fr.cyu.rt.business.model.EventType import EventType


class Event:
    def __init__(self):
        self.eventTypeID = 0
        self.eventTypeLabel = EventType(0).name
        self.sensorTypeID = 0
        self.sensorTypeLabel = SensorType(0).name
        self.timestamp = time.time()
        self.dateTime = datetime.now()
        self.measurement = 'None'
        self.img = 'None'

    def __init__(self, eventTypeID=-1, sensorTypeID=-1, timestamp=time.time(), measure='None', img='None'):
        if eventTypeID in EventType._value2member_map_.keys():
            self.eventTypeID = eventTypeID
            self.eventTypeLabel = EventType(eventTypeID).name
        else:
            self.eventTypeID = 0
            self.eventTypeLabel = EventType(0).name

        if sensorTypeID in SensorType._value2member_map_.keys() :
            self.sensorTypeID = sensorTypeID
            self.sensorTypeLabel = SensorType(sensorTypeID).name
        else :
            self.sensorTypeID = 0
            self.sensorTypeLabel = SensorType(0).name

        self.timestamp = timestamp
        self.dateTime = datetime.fromtimestamp(timestamp)
        self.measure = measure
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
               f'{self.timestamp} {self.dateTime} {self.measure} {self.img}'