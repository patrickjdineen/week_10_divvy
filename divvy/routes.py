from divvy import db, app
from flask import Flask, jsonify, request
from divvy.models import Divvy

@app.route('/average',methods= ['GET'])
def get_average():
    data = request.get_json()
    start_time=data['start_time']
    end_time = data['end_time']
    trips = Divvy.query.filter(Divvy.starttime >=start_time, Divvy.stoptime <= end_time)
    output = []
    total_time= 0
    num_trips = 0
    for trip in trips:
        num_trips +=1
        total_time += trip.trip_duration
    return jsonify({"Average Time":str(total_time/num_trips)})