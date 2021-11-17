import csv
import sys

from Ex1.src.Building import Building
from Ex1.src.InputCalls import InputCalls

DOWN = -1
REST = 0
UP = 1

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


def allocate(self):
    global allocated_elev
    for call_i in range(len(self.calls)):
        src = int(float(self.calls[call_i][2]))
        dest = int(float(self.calls[call_i][3]))
        if src > self.max_floor or src < self.min_floor or dest > self.max_floor or dest < self.min_floor:
            raise Exception("Out of the range!")
        min_time = sys.maxsize
        for cur_elev in range(len(self.elevators)):
            if location[cur_elev] == src:
                allocated_elev = cur_elev
                break
            toSrc.insert(cur_elev, calculateToSrc(self, cur_elev, src))
            fromSrc.insert(cur_elev, calculateFromSrc(self, dest, cur_elev, src))
            temp_time = toSrc[cur_elev] + fromSrc[cur_elev]
            if temp_time < min_time:
                min_time = temp_time
                allocated_elev = cur_elev
        addstops(src, dest, allocated_elev)
        self.calls[call_i][5] = allocated_elev


def calculateToSrc(self, cur_elev, src):
    pass_num = PassNumSrc(cur_elev, src)
    dif = abs(location[cur_elev] - src)
    closeTime = self.elevators[cur_elev].get("_closeTime") * pass_num
    startTime = self.elevators[cur_elev].get("_startTime") * (pass_num + 1)
    stopTime = self.elevators[cur_elev].get("_stopTime") * (pass_num + 1)
    openTime = self.elevators[cur_elev].get("_openTime") * (pass_num + 1)
    speed = self.elevators[cur_elev].get("_speed")
    toSrc = closeTime + startTime + dif / speed + stopTime + openTime
    return toSrc


def PassNumSrc(cur_elev, src):
    pass_num = 0
    if status[cur_elev] != DOWN:
        for i in range(len(num_of_stops[cur_elev])):
            if src > num_of_stops[cur_elev][i]:
                pass_num = pass_num + 1
    else:
        for i in range(len(num_of_stops[cur_elev])):
            if src < num_of_stops[cur_elev][i]:
                pass_num = pass_num + 1
    return pass_num


def PassNumDest(dest, cur_elev):
    pass_num = 0
    if status[cur_elev] != DOWN:
        for i in range(len(num_of_stops[cur_elev])):
            if dest > num_of_stops[cur_elev][i]:
                pass_num = pass_num + 1
    else:
        for i in range(len(num_of_stops[cur_elev])):
            if dest < num_of_stops[cur_elev][i]:
                pass_num = pass_num + 1
    return pass_num
