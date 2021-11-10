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