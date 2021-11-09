from typing import final


class Elevator:

    def __init__(self, id:int, speed:float, minFloor:int, maxFloor:int, closeTime:float,
                 openTime:float, startTime:float, stopTime:float):
        self._id=id
        self._speed = speed
        self._minFloor = minFloor
        self._maxFloor = maxFloor
        self._closeTime = closeTime
        self._openTime = openTime
        self._startTime = startTime
        self._stopTime = stopTime
        self._currState = 0

    def __str__(self) -> str:
        return f"id: {self._id}, speed: {self._speed} , minFloor: {self._minFloor}, maxFloor: {self._maxFloor}, " \
               f"closeTime: {self._closeTime}, openTime: {self._openTime}, startTime: {self._startTime}, " \
               f"stopTime: {self._stopTime}, currPos: {0}"

    def get_id(self):
        return self._id;

    def get_speed(self):
        return self._speed;

    def get_min_floor(self):
        return self._minFloor;

    def get_max_floor(self):
        return self._maxFloor;

    def get_close_time(self):
        return self._closeTime;

    def get_open_time(self):
        return self._openTime;

    def get_start_time(self):
        return self._startTime;

    def get_stop_time(self):
        return self._stopTime;
