class Elevator:

    def __init__(self, elevator):
        self._id = int(elevator["_id"])
        self._speed = float(elevator["_speed"])
        self._minFloor = float(elevator["_minFloor"])
        self._maxFloor = float(elevator["_maxFloor"])
        self._closeTime = float(elevator["_closeTime"])
        self._openTime = float(elevator["_openTime"])
        self._startTime = float(elevator["_startTime"])
        self._stopTime = float(elevator["_stopTime"])
        self.CallsElv = []
        self.pos = 0

    def callActive(self, call):
        self.callsElv.append(call)

    def waitingTime(self, source, desT):
        return abs(source - desT) / (self.stopTime + self.startTime + self.openTime + self.closeTime + self.speed)


    @property
    def id(self):
        return self._id

    @property
    def speed(self):
        return self._speed

    @property
    def minFloor(self):
        return self._minFloor

    @property
    def maxFloor(self):
        return self._maxFloor

    @property
    def closeTime(self):
        return self._closeTime

    @property
    def openTime(self):
        return self._openTime

    @property
    def startTime(self):
        return self._startTime

    @property
    def stopTime(self):
        return self._stopTime
