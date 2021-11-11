import csv
import sys
from typing import final

LEVEL: final[int] = 0
DOWN: final[int] = -1
UP: final[int] = 1


class callForElev:

    def __init__(self, time: float = 0, src: int = 0, dst: int = 0, **kwargs):
        self.arrive = time
        self.done_time = sys.float_info.max
        self.going_to_dst = -1
        self.src = src
        self.dst = dst
        self.state = UP if dst > src else DOWN
        self.allocated_to = -1