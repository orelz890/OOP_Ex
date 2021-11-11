from select import poll

from Elevator import Elevator
from typing import final
from CallForElev import callForElev

LEVEL: final[int] = 0
DOWN: final[int] = -1
UP: final[int] = 1


class Structure:

    def __init__(self, e: Elevator):
        self.id = id
        self.my_calls_up = []
        self.my_calls_down = []
        self.total_up_time = 0
        self.total_down_time = 0
        self.pass_num = 0
        self.state = LEVEL
        self.farthest_dst = 0

        self.init_call = callForElev.__init__()
        self.init_state = UP
        self.min_floor = e.min_floor
        self.max_floor = e.max_floor
        self.elev_pos_in_time = 0
        self.elev_pos = 0
        self.call_log = [e.max_floor - e.min_floor]
        for i in range(0, e.max_floor - e.min_floor, 1):
            self.call_log[i] = []
