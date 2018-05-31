import logging
import requests

from get_nearby_takeaways import get_random_recommendation

USER_LOCATION_LINK = "{api_endpoint}/v1/devices/{device_id}/settings/address/countryAndPostalCode"


def lambda_handler(event, session):
    logging.info("Received request")

    request_type = event['request'].get('type')
    permissions = event['context']['System']['user'].get('permissions')
    if not permissions:
        location_permission = False
    else:
        location_permission = True

    title = "Take Aways"
    response_message = "Welcome to Take Aways!"
    reprompt = False
    if request_type == 'LaunchRequest':
        response_message = (
            "Please ask a question like: What are take aways options for lunch?"
        )
        should_end_session = False
        reprompt = True
    elif request_type == 'IntentRequest':
        request_intent = event['request']['intent']['name']
        if request_intent == 'getRandomNearby':
            if location_permission:
                response_message = get_random_nearby(event)
    should_end_session = True
    return build_response(card_title=title,
                          card_content=response_message,
                          output_speech=response_message,
                          should_end_session=should_end_session,
                          location_permission=location_permission,
                          reprompt=reprompt)


def get_random_nearby(event):
    permissions = event['context']['System']['user'].get('permissions')

    api_endpoint = event['context']['System']['apiEndpoint']
    device_id = event['context']['System']['device']['deviceId']
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
    return speech_text


def build_response(
        card_title="Take Aways",
        card_content="Returns nearby open take away places",
        output_speech="Welcome to Take Aways",
        should_end_session=True,
        location_permission=True,
        reprompt=False):
    """
    Builds a valid ASK response based on the incoming attributes.
    """
    ask_response = {
        "version": "1.0",
        "response": {
            "card": {
                "type": "Simple",
                "title": card_title,
                "content": card_content,
            },
            "outputSpeech": {
                "type": "PlainText",
                "text": output_speech
            },
            "shouldEndSession": should_end_session
        }
    }
    if not location_permission:
        ask_response = add_permission_request(ask_response, output_speech)
    if reprompt:
        ask_response = add_reprompt(ask_response)
    return ask_response


def add_permission_request(response, original_message):
    """
    Changes the response card to ask for location permissions and adds to the
    output speech to alert user to enable location settings for app.
    """
    permission_card = {
        "type": "AskForPermissionsConsent",
        "permissions": [
            "read::alexa:device:all:address:country_and_postal_code"
        ]
    }
    permission_message = (
        "To get nearby recommendations,"
        "Please enable location access in your alexa app for Take Aways skill."
    )
    response['response']['card'] = permission_card
    new_message = '. '.join([original_message, permission_message])
    response['response']['outputSpeech']['text'] = new_message

    return response


def add_reprompt(response):
    """
    Adds a response message to tell the user to ask their question again.
    """
    response['response']['reprompt'] = {
        "outputSpeech": {
            "type": "PlainText",
            "text": "Please ask your Take Aways question"
        }
    }
    return response
