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
        for i in range(0, len(self.calls), 1):
            self.allocate(i)
        writeToFile.Write.save_to_file("Ex1_Ans")

    def allocate(self, call_indx) -> None:
        fastest = (len(self.elevs) + 1) * random()
        best_time = sys.float_info.max
        for i in range(0, len(self.elevs), 1):
            curr_elev_time = self.time_cal(self.b.elevators[str(i)], i, call_indx, False)
            if curr_elev_time < best_time:
                best_time = curr_elev_time
                fastest = i
        self.update_fastest(fastest, call_indx)
        self.elevs[fastest].curr_total_time += best_time
        self.calls[call_indx].allocated_to = fastest

    def update_fastest(self, elev_indx: int, call_indx: int) -> None:
        # Reversing the critical changes:
        elev = self.elevs[elev_indx]
        new_call = self.calls[call_indx]
        elev.elev_pos_in_time = 0
        elev.elev_pos = 0
        elev.num_of_done_calls = 0
        elev.passenger_num = 0
        elev.num_of_calls_added += 1
        elev.call_log[new_call.src].append(new_call)
        elev.call_log[new_call.dst].append(new_call)

    def time_cal(self, e: Elevator, elev_indx: int, call_indx: int) -> float:
        elev = self.elevs[elev_indx]
        new_call = self.calls[call_indx]
        total_time_before_change = elev.curr_total_time
        for i in range(0, len(elev.call_log), 1):
            for j in range(0, len(elev.call_log[i]), 1):
                elev.call_log[i][j].done_time = sys.float_info.max
                elev.call_log[i][j].going_to_dst = -1
        # Checking if the call is in the elev range:
        if (e.min_floor <= new_call.src <= e.max_floor) \
                and (e.min_floor <= new_call.src <= e.max_floor):
            src = new_call.src
            dst = new_call.dst
            # Dealing with the first ever call of this elev
            if elev.state == LEVEL:
                return self.init_call_cal(src, dst, call_indx, elev_indx, e)

            # Calculating the first movement to one of the edges:
            elev.call_log[new_call.src].append(new_call)
            elev.call_log[new_call.dst].append(new_call)
            elev.curr_total_time += self.init_call_cal(elev.init_call.src, elev.init_call.dst, call_indx, elev_indx, e)
            elev.elev_pos_in_time += self.init_call_cal(elev.init_call.src, elev.init_call.dst, call_indx, elev_indx, e)
            # UP case:
            if self.elevs[elev_indx].state == UP:
                for i in range(elev.init_call.src, len(e.max_floor - e.min_floor), 1):
                    elev.elev_pos = i
                    self.checking_the_call(e, elev_indx, i)
                self.back_and_forth_check(e, elev_indx, call_indx, DOWN)
            # Down case
            elif self.elevs[elev_indx].state == DOWN:
                for i in range(elev.init_call.src, 0, -1):
                    elev.elev_pos = i
                    self.checking_the_call(e, elev_indx, i)
                self.back_and_forth_check(e, elev_indx, call_indx, UP)

            # Reversing the critical changes:
            elev.call_log[new_call.src].remove(new_call)
            elev.call_log[new_call.dst].remove(new_call)
            total_after = elev.curr_total_time
            elev.curr_total_time = total_time_before_change

            # Returning the additional time (if it will be allocated to this elev)
            return total_after - total_time_before_change
        # If the call is not in the elev range:
        else:
            return sys.float_info.max

    # Checking the call and its addition to the time cal
    def checking_the_call(self, e: Elevator, elev_indx: int, i: int) -> None:
        elev = self.elevs[elev_indx]

        # There are no elements in this cell
        if len(elev.call_log[i]) == 0:
            return

        # Increasing the elev_pos_in_time by one floor time
        elev.elev_pos_in_time += self.time_cal_helper(elev.elev_pos, i + e.min_floor, 0, e)
        elev.elev_pos = i + e.min_floor

        for j in range(0, len(elev.call_log[i]), 1):
            # Checking if the caller can catch the elev in time
            if elev.elev_pos_in_time >= elev.call_log[i][j].arrive:
                curr_src = elev.call_log[i][j].src
                curr_dst = elev.call_log[i][j].dst
                # If the call is here because its src is in the current pos of the elev:
                if ((i + e.min_floor) == curr_src) and (elev.call_log[i][j].done_time == sys.float_info.max) \
                        and (elev.call_log[i][j].going_to_dst == -1):
                    elev.call_log[i][j].going_to_dst == 1
                    elev.passenger_num += 1
                    elev.elev_pos_in_time += self.time_cal_helper(0, 0, self.elevs[elev_indx].passenger_num, e)
                    elev.curr_total_time = elev.elev_pos_in_time

                # If the call is here because its dst is in the current pos of the elev:
                elif ((i + e.min_floor) == curr_dst) and (elev.call_log[i][j].going_to_dst == 1) \
                        and (elev.call_log[i][j].done_time == sys.float_info.max):
                    elev.elev_pos_in_time += self.time_cal_helper(0, 0, elev.passenger_num, e)
                    elev.curr_total_time = elev.elev_pos_in_time
                    elev.call_log[i][j].done_time = elev.elev_pos_in_time
                    elev.num_of_done_calls += 1
                    elev.passenger_num -= 1

    def back_and_forth_check(self, e: Elevator, elev_indx: int, call_indx: int, state: int) -> None:
        elev = self.elevs[elev_indx]
        if elev.num_of_calls_added + 1 == elev.num_of_done_calls:
            return
        if state == UP:
            for i in range(elev.elev_pos, e.max_floor, 1):
                elev.elev_pos = i
                self.checking_the_call(e, elev_indx, i)
            self.back_and_forth_check(e, elev_indx, call_indx, DOWN)
        if state == DOWN:
            for i in range(elev.elev_pos, 0, -1):
                elev.elev_pos = i
                self.checking_the_call(e, elev_indx, i)
            self.back_and_forth_check(e, elev_indx, call_indx, UP)

    def init_call_cal(self, src: int, dst: int, call_indx: int, elev_indx: int, e: Elevator) -> float:
        elev = self.elevs[elev_indx]
        new_call = self.calls[call_indx]
        to_src = self.time_cal_helper(0, src, 1, e)
        if to_src < new_call.arrive:
            to_src = 0
        else:
            to_src -= new_call.arrive
        to_dst = self.time_cal_helper(src, dst, 1, e)
        elev.init_call = new_call
        elev.state = -1
        if new_call.state == UP:
            self.elevs[elev_indx].state == UP
        else:
            self.elevs[elev_indx].state == DOWN
        return to_src + to_dst

    def time_cal_helper(self, src: int, dst: int, pass_num: int, e: Elevator) -> float:
        max = src if src > dst else dst
        min = src if src < dst else dst
        return (max - min) / e.speed + pass_num * (e.close_time + e.open_time + e.start_time + e.stop_time)
