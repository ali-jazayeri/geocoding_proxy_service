import argparse
from flask import Flask, jsonify
from third_party_services.google_service import GoogleService
from third_party_services.here_serivce import HereService

app = Flask(__name__)

# This is the main entry point of the application. Flask is used for providing API service.


# GET route for API
@app.route('/<string:address>', methods=['Get'])
def geocoding_service(address):
    location = get_location_with_failover(address)
    if location is None:
        return jsonify({'message': 'None of the services responded.'})
    print('Lat: ' + str(location.latitude))
    print('Lng: ' + str(location.longitude))
    return location.serialize()


# Handles the failover of the services. If the primary geocoding service does not return a result or there is a network
# error when accessing the service, the code falls back to use the secondary service.
def get_location_with_failover(address):

    # A sorted list of defined services. The first one will be tried first.
    defined_services = [
        HereService(),
        GoogleService()]

    # Try each defined service and the first time that a service responds correctly, return.
    for api_service in defined_services:
        loc = api_service.get_location(address)
        if loc is None:
            print ('Service ' + api_service.service_name() + ' did not respond.')
        else:
            print('Location found by service ' + api_service.service_name())
            return loc

    # If none of the defined services responded, return None.
    print('None of the services responded.')
    return None


if __name__ == "__main__":
    print("Starting Geocoding Proxy Service...")
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, dest='port', default=8081, help='The port number on localhost.')
    args = parser.parse_args()
    port = args.port

    print("Geocoding Proxy Service is running...")

    # For debugging, the following line can be used.
    # app.run(debug=True, port=port)
    app.run(port=port)
    print("Geocoding Proxy Service is stopped...")
