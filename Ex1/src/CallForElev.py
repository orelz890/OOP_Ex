import csv

class callForElev:

    def __init__(self,time:float,src:int,dst:int):
        self._arrive = time
        self._src = src
        self._dst = dst
        self.state = 0;
        self.allocatedTo = -1;

    def get_arrive_time(self):
        return self._arrive

    def get_src(self):
        return self._src

    def get_dst(self):
        return self._dst

    def set_allocated(self):
        return self.allocatedTo
