import csv
import sys
from Ex1.src.Building import Building
from Ex1.src.InputCalls import InputCalls

DOWN = -1
LEVEL = 0
UP = 1

cur_location = []
status = []
to_src_times = []
from_src_times = []
each_elev_stops = []


class Offline:

    def __init__(self, jsonfile: str, calls_name: str, out_name: str):
        self.b = Building(jsonfile)
        self.calls = InputCalls(calls_name).calls
        self.elevators = self.b.elevators
        self.min_floor = self.b.min_floor
        self.max_floor = self.b.max_floor
        for elev in range(len(self.elevators)):
            cur_location.append(0)
            status.append(LEVEL)
            each_elev_stops.append([])
        allocate(self)
        try:
            with open(out_name, 'w', newline="") as f:
                write = csv.writer(f)
                write.writerows(self.calls)
        except IOError as e:
            print(e)


def allocate(self):
    for call_num in range(len(self.calls)):
        src = int(self.calls[call_num][2])
        dest = int(self.calls[call_num][3])
        min_time = sys.maxsize
        number_of_elev = len(self.elevators)
        for cur_elev in range(number_of_elev):
            if cur_location[cur_elev] == src:
                allocated_elev = cur_elev
                break
            elev = self.elevators[cur_elev]
            if elev["_minFloor"] > src or src > elev["_maxFloor"] \
                    or elev["_minFloor"] > dest or dest > elev["_maxFloor"]:
                continue
            to_src_times.insert(cur_elev, calculate(self, src, cur_elev, cur_location[cur_elev]))
            from_src_times.insert(cur_elev, calculate(self, dest, cur_elev, src))
            temp_time = to_src_times[cur_elev] + from_src_times[cur_elev]
            if temp_time < min_time:
                min_time = temp_time
                allocated_elev = cur_elev
        PickUp(src, dest, allocated_elev)
        self.calls[call_num][5] = allocated_elev


def calculate(self, dest: int, cur_elev: int, src: int):
    stops_num = StopsOnWayToDst(cur_elev, dest)
    max = src if src > dest else dest
    min = src if src < dest else dest
    dif = max - min
    speed = self.elevators[cur_elev].get("_speed")
    closeTime = self.elevators[cur_elev].get("_closeTime")
    startTime = self.elevators[cur_elev].get("_startTime")
    stopTime = self.elevators[cur_elev].get("_stopTime")
    openTime = self.elevators[cur_elev].get("_openTime")
    TimeToDest = (dif / speed) + (closeTime + startTime + stopTime + openTime) * (stops_num)
    return TimeToDest


def StopsOnWayToDst(cur_elev: int, dst: int):
    stops_num = 0
    if status[cur_elev] != DOWN:
        for i in range(len(each_elev_stops[cur_elev])):
            if dst > each_elev_stops[cur_elev][i]:
                stops_num += 1
    else:
        for i in range(len(each_elev_stops[cur_elev])):
            if dst < each_elev_stops[cur_elev][i]:
                stops_num += 1
    return stops_num


def PickUp(src: int, dest: int, allocated_elev: int):
    each_elev_stops[allocated_elev].append(src)
    each_elev_stops[allocated_elev].append(dest)
    if src < dest:
        if len(each_elev_stops[allocated_elev]) == 0:
            status[allocated_elev] = UP
    else:
        if len(each_elev_stops[allocated_elev]) == 0:
            status[allocated_elev] = DOWN
    cur_location[allocated_elev] = dest


if __name__ == '__main__':
    Offline("B5.json", "Calls_d.csv", "out_33.csv")
