# OOP_Ex1

This project is an assignment in the object-oriented course at Ariel University(second year).
The problem in general:
We face with the offline algorithem problem. meaning the algorithem input is a json file named "Bilding.json" and a csv file named "Calls_*.csv"
The first contains all the relevent data about a specific building -  min/max floor and a list of elevators(with the relevent data about them)
The second stores the future calls in a specified time

search of useful Related Sites:

1. https://dergipark.org.tr/tr/download/article-file/539296
2. https://codereview.stackexchange.com/questions/7990/elevator-program 
3. https://github.com/joeblau/sample-elevator-control-system/blob/master/src/main/java/com/joeblau/ecs/impl/Elevator.java
4. https://www.popularmechanics.com/technology/infrastructure/a20986/the-hidden-science-of-elevators/

Our mission:
assigning the most afficient elevator to all the imput calls, meaning reducing the waiting time to a minimum.
and returning a csv file (same format) with the allocate changes for eatch call. 

structure:
lets brake the problem to peices.
First, create a class that receives the input csv, named "InputCalls" && a class for the json file, named "Building".
second, creat a class that returns a csv file with the answer to the algorithem problem, named "Offline"
third, creat a function that calculates && returns the most afficient elevator to a specific call
fourth, creat the calculaiting function
and last ,creat a function that stores all the answers into a csv file

algoritem:
lets assume that all the above is already implemented.
First of all, a couple of rouls:
1. Our solution is based on the status of the elevator. Meaning, if the elevator status is UP for example it can only pick up UP calls.
2. An elevator can not wait for a passenger more then the open doors time.
3. All the elevators start position is on the 0 floor(LEVEL).
4. The elevator has no passengers limit.

The "Offline" algorithem will run through all the calls, and calculate which elevator is the most afficient elevator.
By running through all the elevators in the building and asking, how much time does it take to this specific elevator to complete the current call.
The calculation will consider the open/close time + start/stop time multiplied by the number of passengers on it, for eatch stop.
Plus the time it takes to get to src and from src to dst.
If the answer is lower than the currnt most afficient elev, update the most afficient.
Update the current call allocate_to value to the most afficient.
When the algorithem has finished, we are left with an updated call list.
last, make an updated csv file containing the answers.

How to run the code in cmd after running the program from MyAlgo.py on pycharm:
<FOLDER PATH> java -jar Ex1_checker_V1.2_obf.jar 1111,2222,3333 B5.json out_33.csv out.log


