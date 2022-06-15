import math

def hexagonalFit(X, Y, R):
    return math.ceil((X*Y/math.pow(R,2)) * (2/(3*math.sqrt(3)))) #minimum number of circles based on the stackoverflow algorithm

classRooms = int(input("How many classrooms are to be serviced\n>"))

#arrays for coordinates, Xcoordinates and Ycoordinates of all classrooms respectively
classLocations = []
classLocationsX = []
classLocationsY = []

#inputing all coordinates
for i in range(classRooms):
    classLocations.append([float(input("Enter x coordinate of classroom " + str(i+1) + " >")), float(input("Enter y coordinate of classroom " + str(i+1) + " >"))])
    classLocationsX.append(classLocations[i][0])
    classLocationsY.append(classLocations[i][1])

#defining a minimum cover rectangle to cover all the coordinates
rect = [[max(classLocationsX), max(classLocationsY)], [max(classLocationsX), min(classLocationsY)], [min(classLocationsX), max(classLocationsY)], [min(classLocationsX), min(classLocationsY)]]

width = max(classLocationsX) - min(classLocationsX)
height = max(classLocationsY) - min(classLocationsY)


rng = float(input("Enter Range of router\n>"))

print("The optimal number of routers arranged hexagonally is " + str(hexagonalFit(width, height, rng)))
