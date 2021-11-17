import csv


class InputCalls:

    def __init__(self, fileCalls: str):
        self.calls = self.init_from_file(fileCalls)

    def init_from_file(self, fileName: str):
        try:
            csv_file = open(fileName)
            csvreader = csv.reader(csv_file)
            calls = []
            for row in csvreader:
                calls.append(row)
            csv_file.close()
            return calls

        except IOError as e:
            print(e)
