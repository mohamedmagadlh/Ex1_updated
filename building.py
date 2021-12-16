import json

from Elevator import Elevator


class building:
    _minFloor = None
    _maxFloor = None
    _elevators = []

    def readJson(self, nameFile):
        File = open(nameFile)
        json_dictionary = json.load(File)
        File.close()
        return json_dictionary

    def __init__(self, fileJson):
        Json = self.readJson(fileJson)
        self._minFloor = Json["_minFloor"]
        self._maxFloor = Json["_maxFloor"]
        for elevator in Json["_elevators"]:
            self.elevators.append(Elevator(elevator))

    @property
    def minFloor(self):
        return self._minFloor

    @property
    def maxFloor(self):
        return self._maxFloor

    @property
    def elevators(self):
        return self._elevators

