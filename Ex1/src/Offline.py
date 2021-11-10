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
            self.elevs.append(ElevDataStructure.Structure.__init__())
        for i in self.calls:
            self.allocate(i)
        self.save_to_file("Ex1_Ans")

    # def get_calls(self):
    #     return self.calls

    def allocate(self, call_indx):
        fastest = ((len(self.elevs)+1) *random())
        best_time = sys.float_info.max
        for i in range(0, len(self.elevs), 1):
            curr_elev_time = self.time_cal(self.b.elevators[str(i)], call_indx, False)
            if (curr_elev_time < best_time):
                best_time = curr_elev_time
                fastest = i
        self.calls[call_indx].set_done_time(self.calls[call_indx].get_arrive_time() + best_time)
        curr_elev_time = self.time_cal(self.b.elevators[str(fastest)], call_indx, True)
        self.calls[call_indx].allocated_to = fastest

    def time_cal(self, e:Elevator, call_indx: int, flag: bool):
        src = self.calls[call_indx].get_src()
        dst = self.calls[call_indx].get_dst()
        arrive_time= self.calls[call_indx].get_arrive_time()
        state = self.calls[call_indx].get_state()
        for i in range(0, len(self.elevs.get_my_calls), 1):
            curr_src = self.calls[i].get_src()
            curr_dst = self.calls[i].get_dst()
            curr_arrive_time = self.calls[i].get_arrive_time()
            curr_state = self.calls[i].get_state()








