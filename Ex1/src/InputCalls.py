import csv


class InputCalls:

    def __init__(self, fileCalls: str):
        self.calls = init_from_file(fileCalls)


def init_from_file(fileName: str):
    try:
        calls_csv = open(fileName)
        csvreader = csv.reader(calls_csv)
        calls = []
        for row in csvreader:
            calls.append(row)
        calls_csv.close()
        return calls

    except IOError as e:
        print(e)
