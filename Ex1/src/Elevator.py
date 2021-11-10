from typing import final


class Elevator:

    def __init__(self, id: int = 123456789, speed: float = 1, min_floor: int = 0, max_floor: int = 1,
                 close_time: float = 1, open_time: float = 1, start_time: float = 1, stop_time: float = 1, **kwargs):
        self.id=id
        self.speed = speed
        self.min_floor = min_floor
        self.max_floor = max_floor
        self.close_time = close_time
        self.open_time = open_time
        self.start_time = start_time
        self.stop_time = stop_time
        self.curr_state = 0

    def __str__(self) -> str:
        return f"id: {self.id}, speed: {self.speed} , min_floor: {self.min_floor}, max_floor: {self.max_floor}, " \
               f"close_time: {self.close_time}, open_time: {self.open_time}, start_time: {self.start_time}, " \
               f"stop_time: {self.stop_time}, curr_state: {0}"

    # def get_id(self):
    #     return self._id;
    #
    # def get_speed(self):
    #     return self._speed;
    #
    # def get_min_floor(self):
    #     return self._minFloor;
    #
    # def get_max_floor(self):
    #     return self._maxFloor;
    #
    # def get_close_time(self):
    #     return self._closeTime;
    #
    # def get_open_time(self):
    #     return self._openTime;
    #
    # def get_start_time(self):
    #     return self._startTime;
    #
    # def get_stop_time(self):
    #     return self._stopTime;
