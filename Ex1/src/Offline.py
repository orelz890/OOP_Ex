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

    def __init__(self, buildingName: str, callsName: str):
        self.b = Building(buildingName)
        self.calls = InputCalls(callsName).calls
        self.elevs = []
        for i in range(0, len(self.b.Elevators), 1):
            self.elevs.append(ElevDataStructure.Structure.__init__())
        for i in self.calls:
            self.allocate(i)
        self.save_to_file("Ex1_Ans")

    # def get_calls(self):
    #     return self.calls

    def allocate(self, call_indx):
        fastest = ((len(self.elevs)+1) *random())
        best_time = float(sys.float_info.max)
        for i in range(0,len(self.elevs),1):
            curr_elev_time = self.time_cal(self.b.Elevators[str(i)], call_indx, False)
            if (curr_elev_time < best_time):
                best_time = curr_elev_time
                fastest = i
        self.calls[call_indx].set_done_time(self.calls[call_indx].get_arrive_time() + best_time)  #make set
        curr_elev_time = self.time_cal(self.b.Elevators[str(fastest)], call_indx, True)
        self.calls[call_indx].allocatedTo = fastest

    def time_cal(self, e:Elevator, callIndx:int, flag: bool):
        src = self.calls[callIndx].get_src()
        dst = self.calls[callIndx].get_dst()
        arriveTime= self.calls[callIndx].get_arrive_time()
        state = self.calls[callIndx].get_state()
        for i in range(0, len(self.elevs.get_my_calls),1):   #make get
            currSrc = self.calls[i].get_src()
            currDst = self.calls[i].get_dst()
            currArriveTime = self.calls[i].get_arrive_time()
            currState = self.calls[i].get_state()








