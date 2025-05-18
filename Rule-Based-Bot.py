import re
import random

class RuleBot:
    # Potential Negative Responses
    negative_responses = ("no", "nope", "nah", "naw", "not a chance", "sorry")

    # Exit conversation keywords
    exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later")

    # Random starter questions
    random_questions = (
        "Why are you here?",
        "Are there many humans like you?",
        "What do you consume for sustenance?",
        "Is there intelligent life on this planet?",
        "Does Earth have a leader?",
        "What planet have you visited?",
        "What technology do you have on this planet?"
    )

    def __init__(self):
        self.alienbabble = {
            'describe_planet_intent': r'.*\s*your planet.*',
            'answer_why_intent': r'why\sare.*',
            'about_intellipat': r'.*\s*intellipaat.*',
            # New intents added below
            'greet_intent': r'hi|hello|hey',
            'farewell_intent': r'bye|goodbye|see you',
            'ask_name_intent': r'what\sis\syour\sname.*',
            'weather_intent': r'.*\sweather.*',
        }

    def greet(self):
        self.name = input("What is your name? ")
        will_help = input(
            f"Hi {self.name}, I am Rule-Bot. Will you help me learn about your planet?\n"
        )
        if will_help.lower() in self.negative_responses:
            print("Ok, have a nice Earth day!")
            return
        self.chat()

    def make_exit(self, reply):
        for command in self.exit_commands:
            if reply.lower() == command:
                print("Okay, have a nice Earth day!")
                return True
        return False

    def chat(self):
        no_match_count = 0
        reply = input(random.choice(self.random_questions)).lower()

        while not self.make_exit(reply):
            response = self.match_reply(reply)

            if response in self.no_match_responses:
                no_match_count += 1
            else:
                no_match_count = 0  # Reset on meaningful answer

            if no_match_count >= 2:
                reply = input(random.choice(self.random_questions)).lower()
                no_match_count = 0
            else:
                reply = input(response).lower()

    def match_reply(self, reply):
    for intent, pattern in self.alienbabble.items():
        if re.search(pattern, reply):  # changed from re.match() to re.search()
            if intent == 'describe_planet_intent':
                return self.describe_planet_intent()
            elif intent == 'answer_why_intent':
                return self.answer_why_intent()
            elif intent == 'about_intellipat':
                return self.about_intellipat()
            elif intent == 'greet_intent':
                return self.greet_intent()
            elif intent == 'farewell_intent':
                return self.farewell_intent()
            elif intent == 'ask_name_intent':
                return self.ask_name_intent()
            elif intent == 'weather_intent':
                return self.weather_intent()
    return self.no_match_intent()


    # Existing intent handlers
    def describe_planet_intent(self):
        return "My planet is a vast, cold wasteland with crystalline mountains and glowing lakes."

    def answer_why_intent(self):
        return "I am here to collect information about your species and your planet."

    def about_intellipat(self):
        return "Intellipaat is an e-learning platform that offers technical courses to help humans grow smarter."

    # New intent handlers added
    def greet_intent(self):
        return "Hello there! How can I learn more about your planet today?"

    def farewell_intent(self):
        return "Goodbye! Safe travels on Earth."

    def ask_name_intent(self):
        return "I am Rule-Bot, your friendly alien chatbot."

    def weather_intent(self):
        return "I have not yet learned about your weather systems. Can you tell me more?"

    def no_match_intent(self):
        return random.choice(self.no_match_responses)

    @property
    def no_match_responses(self):
        return (
            "Please tell me more.",
            "Tell me more!",
            "Why do you say that?",
            "I see. Can you elaborate?",
            "Interesting, can you tell me more?",
            "I see. How do you think?",
            "Why?",
            "How do you think I feel when you say that?",
            "That's fascinating! Could you go on?",
            "Hmm, what makes you say that?",
            "Would you care to explain further?",
            "Your planet seems complex. Please continue.",
            "I'm learning so much. What else can you share?",
            "This is new to me. Keep going!",
            "Go on, I'm listening."
        )

# Run the bot
AlienBot = RuleBot()
AlienBot.greet()
