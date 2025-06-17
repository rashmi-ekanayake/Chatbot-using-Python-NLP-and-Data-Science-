import re
import random
import datetime
import tkinter as tk
from tkinter import scrolledtext

class RuleBot:
    negative_responses = ("no", "nope", "nah", "naw", "not a chance", "sorry")
    exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later")
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
        self.no_match_responses = (
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

    def match_reply(self, reply):
        for intent, pattern in self.alienbabble.items():
            if re.search(pattern, reply, re.IGNORECASE):
                if intent == 'describe_planet_intent':
                    return self.describe_planet_intent()
                elif intent == 'answer_why_intent':
                    return self.answer_why_intent()
                elif intent == 'about_intellipat':
                    return self.about_intellipat()
        return random.choice(self.no_match_responses)

    def describe_planet_intent(self):
        return "My planet is a vast, cold wasteland with crystalline mountains and glowing lakes."

    def answer_why_intent(self):
        return "I am here to collect information about your species and your planet."

    def about_intellipat(self):
        return "Intellipaat is an e-learning platform that offers technical courses to help humans grow smarter."


class ChatGUI:
    def __init__(self, bot):
        self.bot = bot
        self.window = tk.Tk()
        self.window.title("RuleBot Chat")

        # Chat display area
        self.chat_area = scrolledtext.ScrolledText(self.window, wrap=tk.WORD, state='disabled', width=60, height=20)
        self.chat_area.pack(padx=10, pady=10)

        # Input box
        self.entry = tk.Entry(self.window, width=50)
        self.entry.pack(side=tk.LEFT, padx=(10, 0), pady=(0, 10))
        self.entry.bind("<Return>", self.send_message)

        # Send button
        self.send_button = tk.Button(self.window, text="Send", command=self.send_message)
        self.send_button.pack(side=tk.LEFT, padx=10, pady=(0, 10))

        self.start_chat()

    def start_chat(self):
        # Start with a random question from the bot
        starter = random.choice(self.bot.random_questions)
        self.display_message("RuleBot: " + starter)

    def display_message(self, message):
        timestamp = datetime.datetime.now().strftime("%H:%M")
        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, f"{message} ({timestamp})\n\n")
        self.chat_area.config(state='disabled')
        self.chat_area.yview(tk.END)

    def send_message(self, event=None):
        user_msg = self.entry.get().strip()
        if not user_msg:
            return

        self.display_message("You: " + user_msg)
        self.entry.delete(0, tk.END)

        if user_msg.lower() in self.bot.exit_commands:
            self.display_message("RuleBot: Okay, have a nice Earth day! Goodbye!")
            self.window.after(2000, self.window.destroy)
            return

        bot_reply = self.bot.match_reply(user_msg)
        self.display_message("RuleBot: " + bot_reply)


if __name__ == "__main__":
    bot = RuleBot()
    gui = ChatGUI(bot)
    gui.window.mainloop()
