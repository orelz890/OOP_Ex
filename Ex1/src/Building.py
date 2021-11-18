import json


class Building:

    def __init__(self, json_building: str):
        self.elevators = []
        self.max_floor = 0
        self.min_floor = 0
        self.init_from_file(json_building)

    def init_from_file(self, file_name: str) -> None:
        try:
            with open(file_name, "r") as f:
                building = json.load(f)
            self.elevators = building["_elevators"]
            self.min_floor = building["_minFloor"]
            self.max_floor = building["_maxFloor"]
            return building
        except IOError as e:
            print(e)
