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
            'about_intellipat': r'.*\s*intellipaat.*'
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
