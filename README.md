# OOP_Ex1

This project is an assignment in the object-oriented course at Ariel University(second year). The problem in 
general: We face with the offline algorithm problem. meaning the algorithm input is a json file named "Building.json" 
and a csv file named "Calls_*.csv". The first contains all the relevant data about a specific building:  min/max 
floor and a list of elevators (with the relevant data about them). The second stores the future calls in a specified 
time. 

Research of useful related sites:

1. https://dergipark.org.tr/tr/download/article-file/539296
2. https://codereview.stackexchange.com/questions/7990/elevator-program 
3. https://github.com/joeblau/sample-elevator-control-system/blob/master/src/main/java/com/joeblau/ecs/impl/Elevator.java
4. https://www.popularmechanics.com/technology/infrastructure/a20986/the-hidden-science-of-elevators/

Our mission:
assigning the most efficient elevator to all the input calls, meaning reducing the waiting time to a minimum.
and returning a csv file (same format) with the allocate changes for each call. 

structure: lets brake the problem to pieces. First, create a class that receives the input csv information, 
named "InputCalls" && a class for the json file, named "Building". Second, creat a class that returns a csv file with 
the answer to the algorithm problem, named "Offline". Third, creat a function that calculates && returns the most 
efficient elevator to a specific call. Fourth, creat the calculating function. Last ,creat a function that stores 
all the answers into a csv file.

algorithm: lets assume that all the above is already implemented. First of all, a couple of rolls:
1. Our solution is based on the status of the elevator. Meaning, if the elevator status is UP for example
   it can only pick up UP calls. 
2. An elevator can not wait for a passenger more then the open doors time.
3. All the elevators start position is on the 0 floor(LEVEL).
4. The elevator has no passengers limit. 

The "Offline" algorithm will run through all the calls, and calculate which elevator is the most efficient. how?
By running through all the elevators in the building and asking, how much time does it take to this specific elevator
to complete the current call.
The calculation will consider the open/close time + start/stop time multiplied by the number of passengers on it,
for each stop. Plus the time it takes to get to src and from src to dst.
If the answer is lower than the current most efficient elevator, update the most efficient.
When the loop has finished, update the current call allocate_to value to the current most efficient.
When the algorithm has finished, we are left with an updated call list.
Lastly, make an updated csv file containing the answers.

How to run the code in cmd after running the program from MyAlgo.py on pycharm:

<FOLDER PATH> java -jar Ex1_checker_V1.2_obf.jar 1111,2222,3333 B5.json out_33.csv out.log
