import csv
import sys

from self import self
from Elevator import Elevator

x={
    "_minFloor": -2,
    "_elevators": [
    {
      "_id": 1,
      "_speed": 1.0,
      "_minFloor": -2,
      "_maxFloor": 10,
      "_closeTime": 2.0,
      "_openTime": 2.0,
      "_startTime": 3.0,
      "_stopTime": 3.0
    },
    {
      "_id": 2,
      "_speed": 2.0,
      "_minFloor": -2,
      "_maxFloor": 10,
      "_closeTime": 2.0,
      "_openTime": 2.0,
      "_startTime": 3.0,
      "_stopTime": 3.0
    }
  ]
}
new_elev_dict={}
x= {
    'elev1':
        Elevator(1,1,2,3,4,5,6,7)
}
i=1
x[str(i)] =1
print(x['1'])
# def save_to_file(self, file_name: str) -> None:
#     try:
#         with open(file_name, "w", newline='') as f:
#             fieldnames = ['cul1', 'cul2', 'cul3', 'cul4', 'cul5', 'cul6']
#             thewriter = csv.DictWriter(f, fieldnames=fieldnames)
#             for i in range(0, len(x), 1):
#                 thewriter.writerow({'cul1': 'Elevator call', 'cul2': 12,
#                                     'cul3': 10, 'cul4': 20,
#                                     'cul5': 0, 'cul6': 1})
#     except IOError as e:
#         print(e)
# save_to_file(self,"file")

# minFloor =0;
# p=[]
# for k,v in x.items():
#     if k== '_minFloor':
#         minFloor = v
#         continue
#     for i in v:
#         print(i)
        # for z in i:
        #     print(z)
# print(new_elev_dict)