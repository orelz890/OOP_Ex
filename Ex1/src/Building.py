from Elevator import Elevator
import json


class Building:

    def __init__(self, file_building: str):
        self.elevators = {}
        self.max_floor = 0
        self.min_floor = 0
        self.init_from_file(file_building)

    def __str__(self) -> str:
        ans = f"minFloor: {self.min_floor}, maxFloor: {self.max_floor}, "
        for i in range(0, len(self.elevators), 1):
            ans += f"Elev{i}: " + str(self.elevators[str(i)])
        return ans

    def __add__(self, other: Elevator):
        self.elevators[other['id']] = other
        return self.elevators

    def init_from_file(self, file_name: str) -> None:
        try:
            with open(file_name, "r") as f:
                data_dict = json.load(f)
                for k, v in data_dict.items():
                    if k == '_minFloor':
                        self.min_floor = v
                        continue
                    if k == '_maxFloor':
                        self.max_floor = v
                        continue
                    for i in v:
                        elev = Elevator(i['_id'], i['_speed'], i['_minFloor'], i['_maxFloor'], i['_closeTime'],
                                        i['_openTime'], i['_startTime'], i['_stopTime'])
                        self.elevators[i['_id']] = elev

        except IOError as e:
            print(e)
