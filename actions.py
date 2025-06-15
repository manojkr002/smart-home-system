from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionTurnOnLight(Action):
    def name(self):
        return "action_turn_on_light"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(text="The light has been turned on.")
        return []

class ActionTurnOffLight(Action):
    def name(self):
        return "action_turn_off_light"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(text="The light has been turned off.")
        return []