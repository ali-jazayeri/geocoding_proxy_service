from third_party_services.bing_service import BingService
from third_party_services.google_service import GoogleService
from third_party_services.here_serivce import HereService


class ServiceFailoverHelper:

    def __init__(self):
        pass

    # Handles the failover of the services. If the primary geocoding service does not return a result or there is a
    # network error when accessing the service, the code falls back to use the secondary service.
    @staticmethod
    def get_location_with_failover(address):

        # A sorted list of defined services. The first one will be tried first.
        defined_services = [
            HereService(),
            GoogleService(),
            BingService()]

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
