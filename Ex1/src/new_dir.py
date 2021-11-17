from Ex1.src.Building import Building
from Ex1.src.InputCalls import InputCalls

time = 1
source = 2
destination = 3
allocated = 5

DOWN = -1
REST = 0
UP = 1

# set permanent variable
location, status, toSrc, fromSrc, num_of_stops = [], [], [], [], []


class Offline:

    def __init__(self, jsonfile: str, calls_name: str, out_name: str):
        self.b = Building(jsonfile)
        self.calls = InputCalls(calls_name).calls
        self.elevators = self.b.elevators
        self.min_floor = self.b.min_floor
        self.max_floor = self.b.max_floor
        for i in range(len(self.elevators)):
            location.append(0)
            status.append(REST)
            num_of_stops.append([])
        allocate(self)
        with open(out_name, 'w', newline="") as f:
            write = csv.writer(f)
            write.writerows(self.calls)