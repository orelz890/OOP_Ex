import Elevator
import json


class Building:

    def __init__(self, file_building: str):
        self.Elevators = {}
        self.max_floor =0
        self.min_floor =0
        self.init_from_file(self, file_building)

    def __str__(self) -> str:
        ans = f"minFloor: {self.min_floor}, maxFloor: {self.max_floor}, "
        for i in range(0, len(self.Elevators), 1):
            ans += f"Elev{i}: " + str(self.Elevators[str(i)])
        return ans

    def __iter__(self):
        return self.Elevators.values().__iter__()

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
                        # elev = Elevator.Elevator(i['_id'], i['_speed'], i['_minFloor'], i['_maxFloor'], i['_closeTime'],
                        #                          i['_openTime'], i['_startTime'], i['_stopTime'])
                        elev = Elevator.Elevator(**v)
                        self.Elevators[str(i['_id'])] = elev

        except IOError as e:
            print(e)