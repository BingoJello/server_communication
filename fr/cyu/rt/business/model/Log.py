class Log:
    def __init__(self):
        self.dateTime = 0
        self.measure = 0

    def __init__(self, dateTime, measure):
        self.dateTime = dateTime
        self.measure = measure

    def getDateTime(self):
        return self.dateTime

    def getMeasure(self):
        return self.measure

    def __str__(self):
        return f'{self.dateTime} {self.measure}'