from Elevator import Elevator
from CallForElev import callForElev

LEVEL = 0
DOWN = -1
UP = 1


class Structure:

    def __init__(self, e: Elevator):
        self.state = LEVEL
        self.min_floor = e.min_floor
        self.max_floor = e.max_floor
        self.init_call = callForElev()
        self.curr_total_time = 0
        self.elev_pos_in_time = 0
        self.num_of_done_calls = 0
        self.num_of_calls_added = 0
        self.passenger_num = 0

        self.curr_calls = []
        self.elev_pos = 0
        self.call_log = []
        for i in range(0, e.max_floor - e.min_floor + 1, 1):
            self.call_log.append([])
