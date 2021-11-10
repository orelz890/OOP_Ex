import csv

class callForElev:

    def __init__(self, time: float = 0, src: int = 0, dst: int = 0, **kwargs):
        self.arrive = time
        self.done_time = -1
        self.src = src
        self.dst = dst
        self.state = 1 if dst > src else -1
        self.allocated_to = -1

    # def get_arrive_time(self):
    #     return self._arrive
    #
    # def get_src(self):
    #     return self._src
    #
    # def get_dst(self):
    #     return self._dst
    #
    # def get_state(self):
    #     return self._state
    #
    # def get_done_time(self):
    #     return self._doneTime
    #
    # def set_allocated(self, allocate:int):
    #     self._allocatedTo = allocate
    #
    # def set_done_time(self, doneTime):
    #     self._doneTime =doneTime