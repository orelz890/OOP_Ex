import sys
from random import random
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
        for i in self.calls:
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
        self.elevs[fastest].call_log[self.calls[call_indx].src].append(self.calls[call_indx])
        self.elevs[fastest].call_log[self.calls[call_indx].dst].append(self.calls[call_indx])
        self.update_fastest()
        self.calls[call_indx].allocated_to = fastest

    def time_cal(self, e: Elevator, elev_indx: int, call_indx: int):
        # Checking if the call is in the elev range:
        if (e.min_floor <= self.calls[call_indx].src <= e.max_floor) \
                and (e.min_floor <= self.calls[call_indx].src <= e.max_floor):
            src = self.calls[call_indx].src
            dst = self.calls[call_indx].dst
            # Dealing with the first ever call of this elev
            if self.elevs[elev_indx].state == LEVEL:
                return self.init_call_cal(src, dst, call_indx, e)
            # Regular case:
            total_time = 0
            if self.calls[call_indx].state == UP:
                for i in range(self.elevs[elev_indx].init_call.src, len(e.max_floor - e.min_floor), 1):
                    self.elevs[elev_indx].elev_pos_in_time = \
                        self.time_cal_helper(self.elevs[elev_indx].elev_pos,i-e.min_floor,0, e)
                    self.elevs[elev_indx].elev_pos = i-e.min_floor

                    # There are no elements in this cell
                    if len(self.elevs[elev_indx].call_log[i]) == 0:
                        continue

                    for j in range(0, len(self.elevs[elev_indx].call_log[i]), 1):
                        curr_src = self.elevs[elev_indx].call_log[i][j].src
                        curr_dst = self.elevs[elev_indx].call_log[i][j].dst
                        if i - e.min_floor == curr_src:
                            pass


            else:
                for i in range(self.elevs[elev_indx].init_call.src, 0, -1):
                    for j in range(0, len(self.elevs[elev_indx].call_log[i]), 1):
                        curr_src = self.elevs[elev_indx].call_log[i][j].src
                        curr_dst = self.elevs[elev_indx].call_log[i][j].dst

            total_time += self.back_and_forth_check(self, e, elev_indx, call_indx)
            return -1
        # If the call is not in the elev range:
        else:
            return sys.float_info.max

    def back_and_forth_check(self, e: Elevator, elev_indx: int, call_indx: int):

        return -1

    def init_call_cal(self, src: int, dst: int, call_indx: int, e: Elevator):
        to_src = self.time_cal_helper(0, src, 1, e)
        if to_src < self.calls[call_indx].arrive:
            to_src = 0
        else:
            to_src -= self.calls[call_indx].arrive
        to_dst = self.time_cal_helper(src, dst, 1, e)
        return to_src + to_dst

    def update_fastest(self):
        pass

    def time_cal_helper(self, src: int, dst: int, pass_num: int, e: Elevator):
        max = src if src > dst else dst
        min = src if src < dst else dst
        return (max - min) / e.speed + pass_num * (e.close_time + e.open_time + e.start_time + e.stop_time)
