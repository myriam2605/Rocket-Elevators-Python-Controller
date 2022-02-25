#from typing_extensions import self


from telnetlib import STATUS


class Column:
    def __init__(self, id, amountOfFloors, amountOfElevators):
        self.ID = id
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
                callButton = CallButton(callbuttonID, buttonFloor, "Up")
                self.callButtonList.append(callButton)
                callbuttonID+=1
            

            if (buttonFloor > 1): 
                callButton = CallButton(callbuttonID, buttonFloor, "Down")
                self.callButtonList.append(callButton)
                callbuttonID+=1
            
            buttonFloor+=1
   

    def createElevators(self, amountOfFloors, amountOfElevators):
        for i in range (amountOfElevators):
            elevatorID = i + 1
            elevator = Elevator(elevatorID, amountOfFloors)
            self.elevatorList.append(elevator)
            print ("elevator")
    

    def requestElevator(self, floor, direction): 
        elevator = self.findElevator(floor, direction)
        elevator.floorRequestList.append(floor)
        elevator.move()
        elevator.operateDoors()
        return elevator
    

    def findElevator(self, requestedFloor, requestedDirection): 
        bestScore = 5
        referenceGap = 10000000
        bestElevator = None
        bestElevatorInformations = None

      
        for i in range (len(self.elevatorList)): 
            if requestedFloor == self.elevatorList[i].currentFloor and self.elevatorList[i].status == "stopped" and requestedDirection == self.elevatorList[i].direction :
            
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
            elif self.elevatorList[i].status == "idle":
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
            
            bestElevator = bestElevatorInformations["bestElevator"]
            bestScore = bestElevatorInformations["bestScore"]
            referenceGap = bestElevatorInformations["referenceGap"]
            
        return bestElevator
          
        
        
    

    def checkIfElevatorIsBetter(self, scoreToCheck, newElevator, bestScore, referenceGap, bestElevator, floor):
        if scoreToCheck < bestScore :
            bestScore = scoreToCheck
            bestElevator = newElevator
            referenceGap = abs(newElevator.currentFloor - floor) 
        elif bestScore == scoreToCheck:
            gap = abs(newElevator.currentFloor - floor)
            if referenceGap > gap:
                bestElevator = newElevator
                referenceGap = gap
            
        
        return {"bestElevator":bestElevator, 
                "bestScore": bestScore,
                "referenceGap": referenceGap}
        
    

class Elevator:
    def __init__(self, id, amountOfFloors):
        self.ID = id
        self.status = "idle"
        self.direction = None
        self.currentFloor = 1
        self.door = Door (id)
        self.floorRequestButtonList = []
        self.floorRequestList = []
        self.screenDisplay = None

        self.createFloorRequestButtons(amountOfFloors)


    def createFloorRequestButtons(self, amountOfFloors):
        buttonFloor = 1
        for i in range (amountOfFloors):
            floorRequestButton = FloorRequestButton(buttonFloor, buttonFloor)
            self.floorRequestButtonList.append(floorRequestButton)
            buttonFloor =i + 1

    def requestFloor(self, floor):
        self.floorRequestList.append(floor)
        self.move()
        self.operateDoors()


    def move(self):
        while len (self.floorRequestList) != 0:
            destination = self.floorRequestList[0]
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
            self.floorRequestList.pop()
        
        self.status = "idle"

    def sortFloorList(self):
        if self.direction == "up":
           self.floorRequestList.sort()
        else:
            self.floorRequestList.reverse()
        
    

    def operateDoors(self):
        self.door.status = "opened"
        if self.status == "moving":
           self.door="closed" 

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
    def __init__(self, id):
        self.ID = id
        self.status= "closed"
