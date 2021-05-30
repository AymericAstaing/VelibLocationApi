from math import sin, cos, sqrt, atan2, radians

def findDistanceBetweenTwoCoordinate(currentPosition, station):
    R = 6373.0
    lat1 = radians(currentPosition.latitude)
    lon1 = radians(currentPosition.longitude)
    lat2 = radians(station.gps.latitude)
    lon2 = radians(station.gps.longitude)
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    print("Result:", distance)
    print("Should be:", 278.546, "km")

#def findNext(currentPosition, station, currentList)


def find10ClothestStations(currentPosition, stations):
	currentList = []
	clothestStations = []
	return 0
	for station in stations:
		print(station.gps.latitude)