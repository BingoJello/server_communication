from enum import Enum


class SensorType(Enum):
    NONE = -1
    CAMERA = 0
    BUTTON = 1
    DISTANCE = 2