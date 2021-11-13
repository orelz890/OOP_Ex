import csv
import json
import sys
from random import random

import CallForElev
import ElevDataStructure
import writeToFile
from Building import Building
from Elevator import Elevator
from InputCalls import InputCalls
from typing import final

LEVEL: final[int] = 0
DOWN: final[int] = -1
UP: final[int] = 1


class Offline:

    def __init__(self, building_name: str, calls_name: str):
        self.b = Building(building_name)
        self.calls = InputCalls(calls_name).calls
        self.elevs = []

        for i in range(0, len(self.b.elevators), 1):
            self.elevs.append(ElevDataStructure.Structure.__init__(self.b.elevators[i]))
        for i in range(0, len(self.calls), 1):
            self.allocate(i)
        writeToFile.Write.save_to_file("Ex1_Ans")

    def allocate(self, call_indx):
        fastest = (len(self.elevs) + 1) * random()
        best_time = sys.float_info.max
        for i in range(0, len(self.elevs), 1):
            curr_elev_time = self.time_cal(self.b.elevators[str(i)], i, call_indx)
            if curr_elev_time < best_time:
                best_time = curr_elev_time
                fastest = i
        self.update_fastest(fastest, call_indx)              #Fill
        self.calls[call_indx].allocated_to = fastest

    def time_cal(self, e: Elevator, elev_indx: int, call_indx: int):
        total_time_before_change = self.elevs[elev_indx].curr_total_time
        new_call = self.calls[call_indx]
        elev = self.elevs[elev_indx]
        elev.curr_calls.append(new_call)
        if (e.min_floor <= new_call.src <= e.max_floor) \
                and (e.min_floor <= new_call.src <= e.max_floor):
            for i in elev.curr_calls:
                src = elev.curr_calls[i].src
                dst = elev.curr_calls[i].dst


        elev.curr_calls.remove(new_call)
        after_change_time = elev.curr_total_time
        elev.curr_total_time = total_time_before_change
        return after_change_time - total_time_before_change

    def time_cal_helper(self, src: int, dst: int, pass_num: int, e: Elevator):
        max = src if src > dst else dst
        min = src if src < dst else dst
        return (max - min) / e.speed + pass_num * (e.close_time + e.open_time + e.start_time + e.stop_time)
