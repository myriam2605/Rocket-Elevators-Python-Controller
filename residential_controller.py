#from typing_extensions import self


class Column:
    def __init__(self, id, amountOfFloors, amountOfElevators):
        self.ID = id
        self.amountOfFloors = amountOfFloors  
        self.amountOfElevators = amountOfElevators
        self.status = "online"
        self.elevatorList = []
        self.callButtonList = []
        self.createElevators (amountOfFloors, amountOfElevators)
        self.createCallButtons (amountOfFloors)



    def createCallButtons(self, amountOfFloors): 
        buttonFloor = 1
        callbuttonID = 0

        for i in range (amountOfFloors):

            if (buttonFloor < amountOfFloors): 
                #let callbuttonID = i + 1
                callButton = CallButton(callbuttonID, "OFF", buttonFloor, "Up")
                self.callButtonList.append(callButton)
                callbuttonID+=1
            

            if (buttonFloor > 1): 
                #let callbuttonID = i + 1
                callButton = CallButton(callbuttonID, "OFF", buttonFloor, "Down")
                #callbuttonID--
                # return this.callButtonList.push(callButton)
                self.callButtonList.push(callButton)
                callbuttonID+=1
            
            buttonFloor+=1
   

    def createElevators(self, amountOfFloors, amountOfElevators):
        for i in range (amountOfFloors):
            elevatorID = i + 1
            elevator = Elevator(elevatorID, amountOfFloors)
            self.elevatorList.append(elevator)
        
    

    def requestElevator(self, floor, direction): 
        elevator = self.findElevator(floor, direction)
        #console.log(elevator);
        elevator.floorRequestList.append(floor)
        elevator.move()
        elevator.operateDoors()
        print (elevator)
    

    def findElevator(self, requestedFloor, requestedDirection): 
        bestScore = 5
        referenceGap = 10000000
        bestElevator
        bestElevatorInformations

        #this.elevatorList.forEach(function (elevator)
        
        for i in range (elevatorList): 
            if requestedFloor == self.elevatorList[i].currentFloor and self.elevatorList[i].status == "idle" and requestedDirection == self.elevatorList[i].direction :
            
                bestElevatorInformations = self.checkIfElevatorIsBetter(
                    1,
                    self.elevatorList[i],
                    bestScore,
                    referenceGap,
                    bestElevator,
                    requestedFloor)
                
            elif requestedFloor > self.elevatorList[i].currentFloor and self.elevatorList[i].status == "up" and requestedDirection == self.elevatorList[i].direction:
                bestElevatorInformations = self.checkIfElevatorIsBetter (
                    2,
                    self.elevatorList[i],
                    bestScore,
                    referenceGap,
                    bestElevator,
                    requestedFloor)

            elif requestedFloor < self.elevatorList[i].currentFloor and self.elevatorList[i].status == "down" and requestedDirection == self.elevatorList[i].direction:
                bestElevatorInformations = self.checkIfElevatorIsBetter (
                    2,
                    self.elevatorList[i],
                    bestScore,
                    referenceGap,
                    bestElevator,
                    requestedFloor)
            elif (self.elevatorList[i].status == "idle"):
                bestElevatorInformations = self.checkIfElevatorIsBetter (
                    3,
                    self.elevatorList[i],
                    bestScore,
                    referenceGap,
                    bestElevator,
                    requestedFloor)
            else :
                bestElevatorInformations = self.checkIfElevatorIsBetter(
                    4,
                    self.elevatorList[i],
                    bestScore,
                    referenceGap,
                    bestElevator,
                    requestedFloor)
            
            bestElevator = bestElevatorInformations.bestElevator
            bestScore = bestElevatorInformations.bestScore
            referenceGap = bestElevatorInformations.referenceGap
            
            print (bestElevator)
            # console.log("-------------");
            # console.log(bestElevatorInformations);
            # console.log(bestScore);
            # console.log("-------------");
        
        
    

    def checkIfElevatorIsBetter(self, scoreToCheck, newElevator, bestScore, referenceGap, bestElevator, floor):
        if scoreToCheck < bestScore :
            bestScore = scoreToCheck
            bestElevator = newElevator
            referenceGap = Math.abs(newElevator.currentFloor - floor)  #print(abs(integer))
        elif bestScore == scoreToCheck:
            #console.log("test")
            gap = abs(newElevator.currentFloor - floor)
            if (referenceGap > gap):
                bestElevator = newElevator
                referenceGap = gap
            
        
        print (bestElevator, 
                bestScore,
                referenceGap)
        
    

class Elevator:
    def __init__(self, id, amountOfFloors):
        self.ID = id
        self.status = "idle"
        self.currentFloor = 1
        self.door = Door()
        self.floorRequestButtonList = []
        self.floorRequestList = []
        self.screenDisplay
        # this.bestElevator;

        self.createFloorRequestButtons(amountOfFloors)


    def createFloorRequestButtons(amountOfFloors):
        buttonFloor = 1
        for i in range (elevatorList):
            floorRequestButton = FloorRequestButton(buttonFloor, buttonFloor)
            self.floorRequestButtonList.append(floorRequestButton)
            buttonFloor +=1

    def requestFloor(floor):
        self.floorRequestList.push(floor)
        self.move()
        self.operateDoors()


    def move():
        while (self.floorRequestList.length != 0):
            destination = self.floorRequestList[0]
            # console.log(destination)
            self.status = "moving"
            if (self.currentFloor < destination):
                self.direction = "up"
                self.sortFloorList()

                while (self.currentFloor < destination):
                    self.currentFloor+=1
                    self.screenDisplay = self.currentFloor
                
            elif (self.currentFloor > destination):
                self.direction = "down"
                self.sortFloorList()
                while (self.currentFloor > destination):
                    self.currentFloor-=1
                    self.screenDisplay = self.currentFloor
            
            self.status = "stopped"
            self.floorRequestList.shift()
        
        self.status = "idle"

    def sortFloorList():
        #console.log(this.requestList, "sortfloorlist");
        if self.direction == "up":
           self.floorRequestList.sort()
        else:
            # this.requestList.sort();
            self.floorRequestList.reverse()
        
        print (self.floorRequestList)
    

    def operateDoors():
        self.door.status = "opened"
        #setTimeout(operateDoors(), 5000)
        self.door.status = "closed"

class CallButton:
    def __init__(self, id, floor, direction):
        self.ID = id
        self.status = "on"  #"on, off"
        self.floor = floor
        self.direction = direction

class FloorRequestButton:
    def __init__(self, id, floor):
        self.ID = id
        self.status = "OFF"
        self.floor = floor

class Door:
    def __init__(self, id, status):
        self.ID = id
        self.status = status
    