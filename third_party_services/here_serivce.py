from location import Location
from third_party_services.third_party_geocoder import ThirdPartyGeocoder


# The Here API for getting geocoding information.
# https://developer.here.com/documentation/geocoder/topics/quick-start-geocode.html
class HereService(ThirdPartyGeocoder):

    def build_uri(self, address):
        app_id = 'sskj1AvJImi58xguN0Eg'
        app_code = 'Z2VfERMvjwDizhMOYsHylQ'
        uri = 'https://geocoder.cit.api.here.com/6.2/geocode.json' + \
                   '?searchtext=' + address + \
                   '&app_id=' + app_id + \
                   '&app_code=' + app_code +\
                   'gen=8'
        return uri

    def get_location_from_api_json_response(self, json_api_response):
        found_loctions = json_api_response['Response']['View']
        if found_loctions.__len__() == 0:
            return None
        location = found_loctions[0]['Result'][0]['Location']['DisplayPosition']
        return Location(location['Latitude'], location['Longitude'])

    def service_name(self):
        return 'Here.com'
