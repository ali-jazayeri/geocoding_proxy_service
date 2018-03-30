from location import Location
from third_party_services.third_party_geocoder import ThirdPartyGeocoder


# The Microsoft Bing Virtual Earth API for getting geocoding information
# https://msdn.microsoft.com/en-us/library/ff817004.aspx
class BingService(ThirdPartyGeocoder):

    def build_uri(self, address):
        key = 'AgHOHjIco32n-FIBWxA5M6eOBP_G7basS6d5HFfHOyvOJCIATVcEmlHZ4KA4kSyN'
        uri = 'http://dev.virtualearth.net/REST/v1/Locations' + \
                     '?q=' + address + \
                     '&key=' + key
        # http://dev.virtualearth.net/REST/v1/Locations?q=1%20Microsoft%20Way%20Redmond%20WA%2098052&o=xml&key=BingMapsKey

        return uri

    def get_location_from_api_json_response(self, json_api_response):
        found_resource_sets = json_api_response['resourceSets']
        if found_resource_sets.__len__() == 0:
            return None
        found_resource = found_resource_sets[0]['resources']
        if found_resource.__len__() == 0:
            return None
        location = found_resource[0]['point']['coordinates']
        return Location(location[0], location[1])

    def service_name(self):
        return 'VirtualEarth.com (Bing)'
