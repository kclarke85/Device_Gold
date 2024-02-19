from geopy.geocoders import Nominatim

def get_location(ip_address):
    geolocator = Nominatim(user_agent="Encounter")
    
    try:
        location = geolocator.geocode(192.168.1.69)
        if location:
            return f"City: {location.address}, Latitude: {location.latitude}, Longitude: {location.longitude}"
        else:
            return "Location not found"
    except Exception as e:

