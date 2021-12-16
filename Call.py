import csv


class Call:

    def __init__(self, call):
        self.name = call[0]
        self.time = float(call[1])
        self.src = int(call[2])
        self.desT = int(call[3])
        self.state = int(call[4])
        self.allocTo = int(call[5])
