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
        writeToFile.Write.save_to_file("Ex1_Ans")

    def allocate(self, call_indx):
        fastest = ((len(self.elevs) + 1) * random())
        best_time = sys.float_info.max
        for i in range(0, len(self.elevs), 1):
            curr_elev_time = self.time_cal(self.b.elevators[str(i)], i, call_indx)
            if curr_elev_time < best_time:
                best_time = curr_elev_time
                fastest = i
        self.calls[call_indx].done_time = self.calls[call_indx].get_arrive_time() + best_time
        self.calls[call_indx].allocated_to = fastest
        if self.calls[call_indx].state == DOWN:
            self.elevs[fastest].my_calls_down.append(self.calls[call_indx])
        else:
            self.elevs[fastest].my_calls_up.append(self.calls[call_indx])
        self.elevs[fastest].total_up_time +=best_time


    def time_cal(self, e: Elevator, elev_indx: int, call_indx: int):
        # Deleting all done calls
        for i in range(0, len(self.elevs[elev_indx].my_calls_up), 1):
            if self.elevs[elev_indx].my_calls_up[i].done_time < self.calls[call_indx].arrive:
                self.elevs[elev_indx].my_calls_up.remove(self.elevs[elev_indx].my_calls_up[i])
            if self.elevs[elev_indx].my_calls_down[i].done_time < self.calls[call_indx].arrive:
                self.elevs[elev_indx].my_calls_down.remove(self.elevs[elev_indx].my_calls_down[i])

        # Dealing with an empty elev
        if len(self.elevs[elev_indx].my_calls_up) == 0:
            return self.resting(e, elev_indx, call_indx)
        # Dealing with regular cases (UP/DOWN)
        if self.elevs[elev_indx].state == UP:
            return self.up_case(e, elev_indx, call_indx)
        return self.down_case(e, elev_indx, call_indx)

    def resting(self, e: Elevator, elev_indx: int, call_indx: int):
        # Dealing with the first ever call of this elev:
        if call_indx == 0:
            to_src = self.time_cal_helper(0, self.calls[call_indx].src, 1, e)
            to_dst = self.time_cal_helper(self.calls[call_indx].src,
                                          self.calls[call_indx].dst, 1, e)
            return to_dst + to_src
        # Dealing with a regular empty list of calls case:
        to_src = self.time_cal_helper(self.elevs[elev_indx].farthest_dst, self.calls[call_indx].src, 1, e)
        to_dst = self.time_cal_helper(self.calls[call_indx].src, self.calls[call_indx].dst, 1, e)
        return to_src + to_dst

    # In progress
    def up_case(self, e: Elevator, elev_indx: int, call_indx: int):
        src = self.calls[call_indx].src
        dst = self.calls[call_indx].dst
        if self.elevs[elev_indx].init_src <= src <= self.elevs[elev_indx].farthest_dst:
            pass_num = 0
            before_call =0
            for i in range(1, len(self.elevs[elev_indx].my_calls_up) - 1, 1):
                if self.elevs[elev_indx].my_calls_up[i].src >= src:
                    before_call =i
                    break
                pass_num += 1
                pass_num = pass_num if self.calls[i].dst > self.calls[call_indx].src else pass_num - 1

            return self.elevs[elev_indx].total_up_time + self.time_cal_helper(self.elevs[elev_indx].farthest_dst, src,
                                                                              pass_num, e) + self.time_cal_helper(src, dst,pass_num, e)

    def down_case(self, e: Elevator, elev_indx: int, call_indx: int):
        pass

    def time_cal_helper(self, src: int, dst: int, pass_num: int, e: Elevator):
        max = src if src > dst else dst
        min = src if src < dst else dst
        return (max - min) / e.speed + pass_num * (e.close_time + e.open_time + e.start_time + e.stop_time)

    def is_possible_to_stop(self, elev_indx, call_indx) -> bool:
        for i in range(0, len(self.elevs[elev_indx].my_calls_up), 1):
            pass
