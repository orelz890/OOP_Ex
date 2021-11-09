import CallForElev
import Elevator
from typing import final
from Offline import Offline

LEVEL: final[int] =0
DOWN: final[int] =-1
UP: final[int] =1

class Structure:

    def __init__(self):
        self.myCalls = []
        self.time = 0
        self.passNum =[]
        self.state = LEVEL
        self.currPos =0