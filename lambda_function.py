# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK for Python.
# Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
# session persistence, api calls, and more.
# This sample is built using the handler classes approach in skill builder.
import logging
import ask_sdk_core.utils as ask_utils
import random
import googlemaps


from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

api_key = '' #Your Google API Key goes here
favorites = [] #Fill this list with your favorites
foodchoices = ["Italian", "Mexican", "Burgers", "Fine Dining", "Chinese", "Japanese", "Pizza"] #Add or remove restaurant types here
lat = (,) #Put your latitude and longitutde here


class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Welcome, I can get you local places to eat."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class PickThreeIntentHandler(AbstractRequestHandler):
    """Handler for Pick Three Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("PickThree")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        if handler_input.request_envelope.request.intent.slots['FoodType'].value:
            slots = handler_input.request_envelope.request.intent.slots
            food = slots['FoodType'].value
        else:
            
            num = random.randint(0,6)
            food = foodchoices[num]
            
        gmaps = googlemaps.Client(key=api_key)
        result = gmaps.places(query=food, location=lat, type="restaurant")
        open = []

        for store in result['results']:
            try:
                if (store.get('opening_hours').get('open_now')) == True:
                    open += [(store.get('name'))]
            except AttributeError:
                open += [(store.get('name'))]
            print(store)
        dinner = len(open)
        top = dinner - 1
        choice1 = random.randint(0, top)
        choice2 = random.randint(0, top)
        while choice1 == choice2:
            choice2 = random.randint(0, top)
        choice3 = random.randint(0, top)
        while choice3 == choice2:
            choice3 = random.randint(0, top)
        
        speak_output = "How about {}, {}, or {}?".format(open[choice1], open[choice2], open[choice3])

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class PickTwoIntentHandler(AbstractRequestHandler):
    """Handler for Pick Two Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("PickTwo")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        if handler_input.request_envelope.request.intent.slots['FoodType'].value:
            slots = handler_input.request_envelope.request.intent.slots
            food = slots['FoodType'].value
        else:
            num = random.randint(0,6)
            food = foodchoices[num]
            
        gmaps = googlemaps.Client(key=api_key)
        result = gmaps.places(query=food, location=lat, type="restaurant")
        open = []

        for store in result['results']:
            try:
                if (store.get('opening_hours').get('open_now')) == True:
                    open += [(store.get('name'))]
            except AttributeError:
                open += [(store.get('name'))]
            print(store)
        dinner = len(open)
        top = dinner - 1
        choice1 = random.randint(0, top)
        choice2 = random.randint(0, top)
        while choice1 == choice2:
            choice2 = random.randint(0, top)
        
        speak_output = "How about {} or {}?".format(open[choice1], open[choice2])
           

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class OneFavIntentHandler(AbstractRequestHandler):
    """Handler for OneFav Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("OneFav")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        food = "{}".format(random.choice(favorites))
        speak_output = "How about {}?".format(food)

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class TwoFavIntentHandler(AbstractRequestHandler):
    """Handler for TwoFav Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("TwoFav")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        food1 = "{}".format(random.choice(favorites))
        food2 = "{}".format(random.choice(favorites))
        while food2 == food1:
            food2 = "{}".format(random.choice(favorites))
        speak_output = "How about {} or {}?".format(food1, food2)

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class ThreeFavIntentHandler(AbstractRequestHandler):
    """Handler for ThreeFav Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("ThreeFav")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        food1 = "{}".format(random.choice(favorites))
        food2 = "{}".format(random.choice(favorites))
        while food2 == food1:
            food2 = "{}".format(random.choice(favorites))
        food3 = "{}".format(random.choice(favorites))
        while food3 == food2:
            food3 = "{}".format(random.choice(favorites))
        speak_output = "How about {}, {}, or {}?".format(food1, food2, food3)

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )



class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "I can help you pick somewhere to eat! How can I help?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Goodbye!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )


class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "You just triggered " + intent_name + "."

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response 
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = "Sorry, I had trouble doing what you asked. Please try again."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


sb = SkillBuilder()

sb.skill_id = "amzn1.ask.skill.ea567276-e1e5-4f4f-9544-adbec87dcc2d"

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(PickThreeIntentHandler())
sb.add_request_handler(PickTwoIntentHandler())
sb.add_request_handler(OneFavIntentHandler())
sb.add_request_handler(TwoFavIntentHandler())
sb.add_request_handler(ThreeFavIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()
