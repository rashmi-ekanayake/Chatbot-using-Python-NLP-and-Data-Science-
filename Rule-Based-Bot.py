import re
import random

class RuleBot:
    ### Potential Negative Responses
    negative_responces = ("no", "nope", "nah", "naw", "not a chance", "sorry")

    ### Exit conversation keywords
    exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later")

    ### Random starter question
    random_questions = (
        "why are you here?",
        "Are there many humans like you?",
        "What do you consume for subtenance?",
        "Is there intelligent life on this planet?",
        "Does earth has a leader?",
        "What planet have u visited?",
        "What technology do u have on this planet?"
    )

    def __init__(self):
        self.alienbabble = {
            'describe_planet_intent': r'.*\s*your planet.*',
            'answer_why_intent': r'why\sare.*',
            'about_intellipat': r'.*\s*intellipaat.*'
        }

    def greet(self):
        self.name = input("What is your name? ")
        will_help = input(
            f"Hi {self.name}, I am Rule-Bot. Will you help me learn about your planet?\n"
        )
        if will_help in self.negative_responces:
            print("Ok, have a nice Earth day!")
            return
        self.chat()

    def make_exit(self, reply):
        for command in self.exit_commands:
            if reply == command:
                print("Okay, have a nice Earth day!")
                return True
        return False

    def chat(self):
        reply = input(random.choice(self.random_questions)).lower()
        while not self.make_exit(reply):
            reply = input(self.match_reply(reply))

    def match_reply(self, reply):
        for key, value in self.alienbabble.items():
            intent = key
            regex_pattern = value
            found_match = re.match(regex_pattern, reply)
            if found_match and intent == 'describe_planet_intent':
                return self.describe_planet_intent()
            elif found_match and intent == 'answer_why_intent':
                return self.answer_why_intent()
            elif found_match and intent == 'about_intellipat':
                return self.about_intellipat()
        return self.no_match_intent()

    def describe_planet_intent(self):
        return "My planet is a vast, cold wasteland with crystalline mountains and glowing lakes."

    def answer_why_intent(self):
        return "I am here to collect information about your species and your planet."

    def about_intellipat(self):
        return "Intellipaat is an e-learning platform that offers technical courses to help humans grow smarter."

    def no_match_intent(self):
        responses = (
            "Please tell me more.\n", "Tell me more!.\n", "Why do you say that?\n", "I see. Can you elaborate?\n",
            "Interesting, can you tell me more?\n", "I see. How do you think?\n", "Why?\n",
            "How do you think I feel when you say that?\n"
        )
        return random.choice(responses)

AlienBot = RuleBot()
AlienBot.greet()
