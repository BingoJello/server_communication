from enum import Enum


class EventType(Enum):
    NONE = -1
    USER_CONTROL_END = 0
    USER_CONTROL = 1
    USER_ACTIVATION = 2
    USER_DEACTIVATION = 3
    ALERT = 4
    ALERT_END = 5
    ALERT_DECISION = 6
    RESET = 7
    LOG = 8
    MOVEMENT_CAMERA = 9
    CONNNECTION = 10
