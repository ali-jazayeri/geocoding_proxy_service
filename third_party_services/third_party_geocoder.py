from abc import abstractmethod
import requests


# The super-class interface (abstract) class that all third party api classes should implement(inherit).
class ThirdPartyGeocoder:

    def __init__(self):
        pass

    # For a given address, find location (containing latitude and longitude).
    def get_location(self, address):
        uri = self.build_uri(address)

        try:
            response = requests.get(uri)
            if response.status_code != 200:
                return None
        except requests.exceptions.ConnectionError:
            return None
        except ValueError:
            return None

        json_object = response.json()
        return self.get_location_from_api_json_response(json_object)

    # For the given address, creates the URI that will be used in rest call.
    @abstractmethod
    def build_uri(self, address):
        pass

    # Finds the latitude and longitude from the given jason response.
    @abstractmethod
    def get_location_from_api_json_response(self, json_api_response):
        pass

    # Name of the service. This is not used in the api. The name will be printed in case the service is down.
    @abstractmethod
    def service_name(self):
        pass
