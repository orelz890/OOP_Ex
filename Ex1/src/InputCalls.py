from CallForElev import callForElev
import csv


class InputCalls:

    def __init__(self, fileCalls: str):
        self.calls = self.init_from_file(fileCalls)

    def init_from_file(self, fileName: str):
        try:
            with open(fileName, 'r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                csv_reader.fieldnames = ['str', 'time', 'src', 'dst', 'state', 'aloocate_to']
                headers = csv_reader.fieldnames
                c = []
                i = 0
                for row in csv_reader:
                    c.append(callForElev(id=i, time=float(row[headers[1]]),
                                         src=int(row[headers[2]]), dst=int(row[headers[3]])))
                    i += 1
                return c
        except IOError as e:
            print(e)
