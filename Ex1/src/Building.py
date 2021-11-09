import Elevator
import json

class Building:

    def __init__(self,fileBuilding : str):
        self.Elevators ={}
        self.init_from_file(self,fileBuilding)

    def __str__(self) -> str:
        ans =f"minFloor: {self._minFloor}, maxFloor: {self._maxFloor}, "
        for i in range(0, len(self.Elevators),1):
            ans+= f"Elev{i} "+str(self.Elevators[str(i)])
        return ans

    def __iter__(self):
        return self.Elevators.values().__iter__()

    def init_from_file(self,file_name:str)->None:
        with open(file_name,"r") as f:
            data_dict = json.load(f)
            for k, v in data_dict.items():
                if k == '_minFloor':
                    self._minFloor = v
                    continue
                if k == '_maxFloor':
                    self._maxFloor = v
                    continue
                for i in v:
                    elev = Elevator.Elevator(i['_id'], i['_speed'], i['_minFloor'], i['_maxFloor'] ,i['_closeTime'] ,
                                    i['_openTime'] ,i['_startTime'] , i['_stopTime'])
                    self.Elevators[str(i['_id'])] = elev

