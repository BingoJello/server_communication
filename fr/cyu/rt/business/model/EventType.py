from enum import Enum


class EventType(Enum):
    NONE = -1
    ALARM = 0
    ALARM_END = 1
    ALARM_DECISION = 2
    USER_ACTIVATION = 3
    USER_DEACTIVATION = 4
    USER_CONTROL = 5
    USER_END_CONTROL = 6
    RESET = 7
    LOG = 8
    MOVEMENT_CAMERA = 9
    CONNNECTION = 10
