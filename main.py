import argparse
from flask import Flask, jsonify
from service_failover_helper import ServiceFailoverHelper

app = Flask(__name__)

# This is the main entry point of the application. Flask is used for providing API service.


# GET route for API
@app.route('/<string:address>', methods=['Get'])
def geocoding_service(address):
    location = ServiceFailoverHelper.get_location_with_failover(address)
    if location is None:
        return jsonify({'message': 'None of the services responded.'})
    print('Lat: ' + str(location.latitude))
    print('Lng: ' + str(location.longitude))
    return location.serialize()


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
