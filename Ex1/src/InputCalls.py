from CallForElev import callForElev
import csv


class InputCalls:

    def __init__(self, fileCalls: str):
        self.calls = self.init_from_file(fileCalls)

    def init_from_file(self, fileName: str):
        try:
            with open(fileName, 'r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                headers = csv_reader.fieldnames
                c = []
                for row in csv_reader:
                    c.append(callForElev(float(row[headers[1]]), int(row[headers[2]]), int(row[headers[3]])))
                return c
        except IOError as e:
            print(e)
