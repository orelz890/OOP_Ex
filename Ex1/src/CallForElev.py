import csv
import sys


class callForElev:

    def __init__(self, time: float = 0, src: int = 0, dst: int = 0, **kwargs):
        self.arrive = time
        self.done_time = sys.float_info.max
        self.src = src
        self.dst = dst
        self.state = 1 if dst > src else -1
        self.allocated_to = -1