import csv

class callForElev:

    def __init__(self,time:float,src:int,dst:int):
        self._arrive = time
        self._doneTime = -1
        self._src = src
        self._dst = dst
        self._state = 1 if dst>src else -1
        self._allocatedTo = -1

    def get_arrive_time(self):
        return self._arrive

    def get_src(self):
        return self._src

    def get_dst(self):
        return self._dst

    def get_state(self):
        return self._state

    def get_done_time(self):
        return self._doneTime

    def set_allocated(self, allocate:int):
        self._allocatedTo = allocate

    def set_done_time(self, doneTime):
        self._doneTime =doneTime