from divvy import app, db

class Divvy(db.Model):
    trip_id	= db.Column(db.Integer, primary_key=True)
    starttime = db.Column(db.DateTime)
    stoptime = db.Column(db.DateTime)
    bikeid = db.Column(db.Integer)
    from_station_id	= db.Column(db.String)
    from_station_name = db.Column(db.String)
    to_station_id = db.Column(db.Integer)
    to_station_name	= db.Column(db.String)
    usertype = db.Column(db.String)
    gender= db.Column(db.String)
    birthday = db.Column(db.String)
    trip_duration = db.Column(db.Integer)