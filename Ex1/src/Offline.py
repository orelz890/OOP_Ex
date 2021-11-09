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

    def get_calls(self):
        return self.calls

    def allocate(self, callindx):
        fastest = ((len(self.elevs)+1) *random())
        bestTime = float(sys.float_info.max)
        for i in range(0,len(self.elevs),1):
            currElevTime = self.time_cal(self.b.Elevators[str(i)], callindx , False)
            if (currElevTime < bestTime):
                bestTime = currElevTime
                fastest = i
        self.calls[callindx].set_done_time(self.calls[callindx].get_arrive_time()+bestTime)  #make set
        currElevTime = self.time_cal(self.b.Elevators[str(fastest)], callindx, True)
        self.calls[callindx].allocatedTo = fastest

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








