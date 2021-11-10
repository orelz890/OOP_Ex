from select import poll

import CallForElev
import Elevator
from typing import final
from Offline import Offline

LEVEL: final[int] = 0
DOWN: final[int] = -1
UP: final[int] = 1


class Structure:

    def __init__(self):
        self.my_calls_up = []
        self.my_calls_down = []
        self.total_time = 0
        self.pass_num = 0
        self.state = LEVEL
        self.init_src = 0
        self.farthest_dst = 0

    # def get_my_calls(self):
    #     return self.myCalls
    #
    # def get_my_calls(self):
    #     return self.myCalls
    #
    # def get_time(self):
    #     return self.time
    #
    # def get_pass_num(self):
    #     return self.passNum
    #
    # def get_state(self):
    #     return self.state
    #
    # def get_curr_pos(self):
    #     return self.currPos
    #
    # def add_to_my_calls(self, call:CallForElev):
    #     self.myCalls.append(call)
    #
    # def set_time(self, time):
    #     self.time = time
    #
    # def set_pass_num(self, pressNum:int):
    #     self.passNum = pressNum
    #
    # def set_state(self, state:int):
    #     self.state = state
    #
    # def set_curr_pos(self, currPos:int):
    #     self.currPos = currPos
    #

