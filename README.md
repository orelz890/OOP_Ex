# OOP_Ex

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
The "Offline" algo will run through all the calls and calculate who is the most afficient elevator.
by running through all the elevator in the building and ask how much time does it take to this specific elevator to complete the current call.
The calculation will consider the open/close time + start/stop time multiplied by the number of passengers on it for eatch stop,
plus the time it takes to get to src and from src to dst.
If the answer is lower than the currnt most afficient elev, update the most afficient.


