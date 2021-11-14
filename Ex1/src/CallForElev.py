import sys

LEVEL = 0
DOWN = -1
UP = 1


class callForElev:

    def __init__(self, id: int = 0, time: float = 0, src: int = 0, dst: int = 0, **kwargs):
        self.arrive = time
        self.done_time = sys.maxsize
        self.id = id
        self.going_to_dst = -1
        self.src = src
        self.dst = dst
        self.state = UP if dst > src else DOWN
        self.allocated_to = -1

    def __str__(self):
        return f"id:{self.id} time:{self.arrive} src:{self.src} dst:{self.dst} state: {self.state} allocate:{self.allocated_to}"

    def __repr__(self):
        return f"id:{self.id} time:{self.arrive} src:{self.src} dst:{self.dst} state: {self.state} allocate:{self.allocated_to}"
