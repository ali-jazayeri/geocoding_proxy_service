from location import Location
from third_party_services.third_party_geocoder import ThirdPartyGeocoder


# The Google API for getting geocoding information
# https://developers.google.com/maps/documentation/geocoding/intro
class GoogleService(ThirdPartyGeocoder):

    def build_uri(self, address):
        key = 'AIzaSyDqG0jPeqNEX5d6ZW87XLuk27pa2VNIrFY'
        uri = 'https://maps.googleapis.com/maps/api/geocode/json' + \
                     '?key=' + key + \
                     '&address=' + address
        return uri

    def get_location_from_api_json_response(self, json_api_response):
        found_locations = json_api_response['results']
        if found_locations.__len__() == 0:
            return None
        location = found_locations[0]['geometry']['location']
        return Location(location['lat'], location['lng'])

    def service_name(self):
        return 'Google.com'
