import random

import googlemaps

api_key = open("/Users/deepenp/key.txt", 'r').read().rstrip()
gmaps = googlemaps.Client(key=api_key)


def get_random_recommendation(postcode):
    geocode_result = gmaps.geocode(postcode)

    lat_long = geocode_result[0]['geometry']['location']
    results = gmaps.places_nearby(lat_long, 700, 'takeaway', None, None, None, None, True, None, "meal_takeaway")

    names = list(map(lambda x: x['name'], results['results']))
    if len(names) == 0:
        return None
    else:
        return random.choice(names)


print(get_random_recommendation('WC2B 5AD'))
