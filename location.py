import flask


# Location class contains latitude and longitude. The API returns a serialized instance of this class. If other
# information is need to be included into the return of the API, the new information can be added to this class.
class Location:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def serialize(self):
        return flask.json.jsonify(self.__dict__)
