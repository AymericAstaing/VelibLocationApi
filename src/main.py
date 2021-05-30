from __future__ import print_function
import pymysql
import json
from app import app
from config import mysql
from flask import jsonify
from calculations import find10ClothestStations
from flask import flash, request

try:
    from types import SimpleNamespace as Namespace
except ImportError:
    from argparse import Namespace


class UserPosition(object):
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

def getCorrectDescription(stationDescription):
    return ((str(stationDescription).replace("\"\"", "\"")).replace("\'", "\""))[24:-2]

def createStationsObjectList(empRows):
	list = []
	for column1 in empRows:
		correctStr = getCorrectDescription(column1)
		list.append(json.loads(correctStr, object_hook=lambda d: Namespace(**d)))
	return list

def getCurrentCoordinateObject(literalCoordinates):
	return (UserPosition(float(literalCoordinates.split(',')[0]), float(literalCoordinates.split(',')[1])))

@app.route('/getVelibArround')
def emp():
	try:
		currentPosition = getCurrentCoordinateObject(str(request.args.get("location")))
		print(currentPosition.latitude)
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT stationDescription FROM VelibLocation")
		empRows = cursor.fetchall()
		stationsList = createStationsObjectList(empRows)
		print(stationsList[0].gps.latitude)
		find10ClothestStations(currentPosition, stationsList)
		respone = jsonify(empRows)
		respone.status_code = 200
		return respone
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

if __name__ == "__main__":
    app.run()