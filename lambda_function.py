import logging

import requests
from flask import Flask
from flask_ask import Ask, statement, context

from get_nearby_takeaways import get_random_recommendation

app = Flask(__name__)

ask = Ask(app, "/")

logging.getLogger("flask_ask").setLevel(logging.DEBUG)
USER_LOCATION_LINK = "{api_endpoint}/v1/devices/{device_id}/settings/address/countryAndPostalCode"


@ask.launch
def launch():
    speech_text = "Hello, you can query like 'Ask take aways for recommendations'"
    return statement(speech_text).simple_card(speech_text)


@ask.intent("getRandomNearby")
def get_random_nearby():
    permissions = context['System']['user'].get('permissions')
    if not permissions:
        return permission_request()

    api_endpoint = context['System']['apiEndpoint']
    device_id = context['System']['device']['deviceId']
    consent_token = "Bearer " + permissions['consentToken']
    headers = {'Authorization': consent_token}
    location_api_link = USER_LOCATION_LINK.format(api_endpoint=api_endpoint, device_id=device_id)
    response = requests.get(location_api_link, headers=headers)
    user_country_code = response.json().get('countryCode')
    user_post_code = response.json().get('postalCode')

    speech_text = "Sorry, We couldn't find any nearby open takeaway for you"
    recommendation = get_random_recommendation(user_country_code + ' ' + user_post_code)
    if recommendation is not None:
        speech_text = "How about " + recommendation + "?"
    return statement(speech_text).simple_card(speech_text)


def permission_request():
    """
    Changes the response card to ask for location permissions and adds to the
    output speech to alert user to enable location settings for app.
    """
    permission_message = (
        "To get nearby recommendations, please enable location access in your alexa app for Take Aways skill."
    )
    return statement(permission_message).consent_card("read::alexa:device:all:address:country_and_postal_code")


def lambda_handler(event, _context):
    return ask.run_aws_lambda(event)


if __name__ == '__main__':
    app.run(debug=True)
