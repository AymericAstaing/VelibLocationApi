import json
from math import sin, cos, sqrt, atan2, radians

def findDistanceBetweenTwoCoordinate(currentPosition, station):
	jsonStr = station.get("stationDescription")
	stationJson = json.loads(jsonStr)
	R = 6373.0
	lat1 = radians(currentPosition.latitude)
	lon1 = radians(currentPosition.longitude)
	lat2 = radians(stationJson["gps"]["latitude"])
	lon2 = radians(stationJson["gps"]["longitude"])
	dlon = lon2 - lon1
	dlat = lat2 - lat1
	a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
	c = 2 * atan2(sqrt(a), sqrt(1 - a))
	distance = R * c
	return distance

def findNextClothestStation(clothestStationListId, currentPosition, stations):
	i = 0
	clothestStationId = -1
	clothestStationDistance = 0

	for station in stations:
		if (clothestStationDistance == 0 and i not in clothestStationListId):
			clothestStationId = i
			clothestStationDistance = findDistanceBetweenTwoCoordinate(currentPosition, station)
			i += 1
			continue
		comparedDistance = findDistanceBetweenTwoCoordinate(currentPosition, station)
		if (comparedDistance < clothestStationDistance and i not in clothestStationListId):
			clothestStationId = i
			clothestStationDistance = comparedDistance
			i += 1
		else:
			i += 1
	clothestStationListId.append(clothestStationId)

def find10ClothestStations(currentPosition, stations):
	i = 0
	clothestStationListId = []
	while i < 10:
		findNextClothestStation(clothestStationListId, currentPosition, stations)
		i += 1
	return clothestStationListId