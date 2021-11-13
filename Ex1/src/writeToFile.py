import csv
import CallForElev
from Offline3 import Offline

class Write:

    def __init__(self, calls: [], file_name: str):
        self.calls = calls
        self.save_to_file(file_name)

    def save_to_file(self, file_name: str) -> None:
        try:
            with open(file_name, "w", newline='') as f:
                fieldnames = ['cul1', 'cul2', 'cul3', 'cul4', 'cul5', 'cul6']
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                for i in range(0, len(self.calls), 1):
                    writer.writerow({'cul1': 'Elevator call', 'cul2': self.calls[i].get_arrive_time(),
                                        'cul3': self.calls[i].get_src(), 'cul4': self.calls[i].get_dst(),
                                        'cul5': 0, 'cul6': self.calls[i].allocatedTo})
        except IOError as e:
            print(e)
