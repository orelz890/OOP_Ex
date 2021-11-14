import csv
import sys
from random import random
import ElevDataStructure
from Elevator import Elevator
from InputCalls import InputCalls
from Building import Building
from CallForElev import callForElev

LEVEL = 0
DOWN = -1
UP = 1


class Offline:

    def __init__(self, B: str, calls_name: str, out_name: str):
        self.b = Building(B)
        self.calls = InputCalls(calls_name).calls
        # self.save_to_file(out_name)
        self.elevs = []
        for i in range(0, len(self.b.elevators), 1):
            self.elevs.append(ElevDataStructure.Structure(self.b.elevators[i]))
        for i in range(0, len(self.calls), 1):
            self.calls[i].allocated_to = self.allocate(i)
        self.save_to_file(out_name)

    def allocate(self, call_indx) -> int:
        new_call = self.calls[call_indx]
        if (self.b.min_floor <= new_call.src <= self.b.max_floor) \
                and (self.b.min_floor <= new_call.dst <= self.b.max_floor):
            fastest = int((len(self.elevs) + 1) * random())
            best_time = sys.maxsize
            for i in range(0, len(self.elevs), 1):
                curr_elev_time = self.time_cal(self.b.elevators[i], i, call_indx)   # call_indx -1???
                if curr_elev_time < best_time:
                    best_time = curr_elev_time
                    fastest = i
            self.update_fastest(fastest, call_indx)
            self.elevs[fastest].curr_total_time += best_time
            return fastest

    def update_fastest(self, elev_indx: int, call_indx: int) -> None:
        # Reversing the critical changes:
        elev = self.elevs[elev_indx]
        new_call = self.calls[call_indx]
        new_call.going_to_dst = -1
        elev.elev_pos_in_time = 0
        elev.elev_pos = 0
        elev.num_of_done_calls = 0
        elev.passenger_num = 0
        elev.num_of_calls_added += 1
        elev.call_log[new_call.src - elev.min_floor].append(new_call)
        elev.call_log[new_call.dst - elev.min_floor].append(new_call)

    def time_cal(self, e: Elevator, elev_indx: int, call_indx: int) -> float:
        if len(self.elevs) == 1:
            return 0
        elev = self.elevs[elev_indx]
        new_call = self.calls[call_indx]
        total_time_before_change = elev.curr_total_time
        for i in range(0, call_indx, 1):
            self.calls[i].done_time = sys.maxsize
            self.calls[i].going_to_dst = -1
        for i in range(0, len(self.elevs[elev_indx].call_log), 1):
            self.elevs[elev_indx].call_log[i] = []
        # Checking if the call is in the elev range:
        if (e.min_floor <= new_call.src <= e.max_floor) \
                and (e.min_floor <= new_call.src <= e.max_floor):
            # Dealing with the first ever call of this elev
            elev.call_log[new_call.src - e.min_floor].append(new_call)
            elev.call_log[new_call.dst - e.min_floor].append(new_call)

            if elev.state == LEVEL:
                elev.curr_total_time = self.init_call_cal(new_call.src, new_call.dst, call_indx, elev_indx, e)
                return elev.curr_total_time

            # Calculating the first movement to one of the edges:
            elev.elev_pos_in_time += elev.curr_total_time

            # UP case:
            if self.elevs[elev_indx].state == UP:
                for i in range(elev.init_call.src, e.max_floor + 1, 1):
                    self.checking_the_call(e, elev_indx, i, call_indx)
                self.back_and_forth_check(e, elev_indx, call_indx, DOWN)

            # Down case
            elif self.elevs[elev_indx].state == DOWN:
                for i in range(elev.init_call.src, e.min_floor - 1, -1):
                    self.checking_the_call(e, elev_indx, i, call_indx)
                self.back_and_forth_check(e, elev_indx, call_indx, UP)

            # Reversing the critical changes:
            elev.call_log[new_call.src - e.min_floor].remove(new_call)
            elev.call_log[new_call.dst - e.min_floor].remove(new_call)
            total_after = elev.curr_total_time
            elev.curr_total_time = total_time_before_change

            # Returning the additional time (if it will be allocated to this elev)
            return total_after - total_time_before_change
        # If the call is not in the elev range:
        else:
            return sys.maxsize

    # Checking the call and its addition to the time cal
    def checking_the_call(self, e: Elevator, elev_indx: int, i: int, call_indx: int) -> None:
        elev = self.elevs[elev_indx]

        # There are no elements in this cell
        if len(elev.call_log[i - elev.min_floor]) == 0:
            return
        flag = False
        for j in range(0, len(elev.call_log[i - elev.min_floor]), 1):
            if elev.call_log[i - elev.min_floor][j].done_time == sys.maxsize:
                flag = True
        if not flag:
            return

        for j in range(0, len(elev.call_log[i - elev.min_floor]), 1):
            # Checking if the caller can catch the elev in time
            curr_src = self.calls[elev.call_log[i - elev.min_floor][j].id].src  # problem
            curr_dst = self.calls[elev.call_log[i - elev.min_floor][j].id].dst  # problem

            if elev.elev_pos_in_time + self.time_cal_helper(elev.elev_pos, i, 1, e) - e.close_time\
                    >= elev.call_log[i - elev.min_floor][j].arrive:
                # Increasing the elev_pos_in_time by one floor time
                elev.elev_pos_in_time += self.time_cal_helper(elev.elev_pos, i, 0, e)
                elev.elev_pos = i
                # print(curr_src)
                # print(curr_src)
                curr_call = self.calls[elev.call_log[i - elev.min_floor][j].id]

                # If the call is here because its src is in the current pos of the elev:
                if (elev.elev_pos == curr_src) and (curr_call.done_time == sys.maxsize) \
                        and (curr_call.going_to_dst == -1):

                    curr_call.going_to_dst == 1
                    elev.passenger_num += 1
                    elev.elev_pos_in_time += self.time_cal_helper(0, 0, self.elevs[elev_indx].passenger_num, e)
                    elev.curr_total_time = elev.elev_pos_in_time

                # If the call is here because its dst is in the current pos of the elev:
                elif (elev.elev_pos == curr_dst) and (curr_call.going_to_dst == 1) \
                        and (curr_call.done_time == sys.maxsize):
                    # print(curr_dst)
                    elev.elev_pos_in_time += self.time_cal_helper(0, 0, elev.passenger_num, e)
                    elev.curr_total_time = elev.elev_pos_in_time
                    curr_call.done_time = elev.elev_pos_in_time
                    elev.num_of_done_calls += 1
                    elev.passenger_num -= 1

    def back_and_forth_check(self, e: Elevator, elev_indx: int, call_indx: int, state: int) -> None:
        elev = self.elevs[elev_indx]
        # print(f"added = {elev.num_of_calls_added} done = {elev.num_of_done_calls}")
        if (elev.num_of_calls_added + 1) <= elev.num_of_done_calls:
            return
        if state == UP:
            for i in range(e.min_floor, e.max_floor + 1, 1):
                self.checking_the_call(e, elev_indx, i, call_indx)
            self.back_and_forth_check(e, elev_indx, call_indx, DOWN)
        if state == DOWN:
            for i in range(e.max_floor, e.min_floor - 1, -1):
                self.checking_the_call(e, elev_indx, i, call_indx)
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
            elev.state == UP
        else:
            elev.state == DOWN
        return to_src + to_dst

    def time_cal_helper(self, src: int, dst: int, pass_num: int, e: Elevator) -> float:
        max = src if src > dst else dst
        min = src if src < dst else dst
        return (max - min) / e.speed + pass_num * (e.close_time + e.open_time + e.start_time + e.stop_time)

    def save_to_file(self, file_name: str) -> None:
        try:
            with open(file_name, "w", newline='') as f:
                fieldnames = ['cul1', 'cul2', 'cul3', 'cul4', 'cul5', 'cul6']
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                for i in range(0, len(self.calls), 1):
                    writer.writerow({'cul1': 'Elevator call', 'cul2': self.calls[i].arrive,
                                     'cul3': self.calls[i].src, 'cul4': self.calls[i].dst,
                                     'cul5': 0, 'cul6': self.calls[i].allocated_to})
        except IOError as e:
            print(e)
