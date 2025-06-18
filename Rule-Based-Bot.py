import re
import random
import datetime
import tkinter as tk
from tkinter import scrolledtext
import pyttsx3


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
        self.engine = pyttsx3.init()
        self.window = tk.Tk()
        self.window.title("RuleBot Chat")

        # Theme state
        self.dark_mode = True

        # Toggle Button
        self.toggle_button = tk.Button(self.window, text="Switch to Light Mode",
                                       command=self.toggle_theme,
                                       bg="#444", fg="white",
                                       bd=0, relief='flat',
                                       font=("Segoe UI", 10, "bold"),
                                       activebackground="#555")
        self.toggle_button.pack(anchor="ne", padx=10, pady=(10, 0))

        # Frame to hold chat area with padding and background color to simulate rounded edges
        self.chat_frame = tk.Frame(self.window, bg="#444444", padx=5, pady=5)
        self.chat_frame.pack(padx=10, pady=10)

        self.chat_area = scrolledtext.ScrolledText(self.chat_frame, wrap=tk.WORD, state='disabled',
                                                   width=60, height=20,
                                                   bd=0, relief='flat',
                                                   font=("Segoe UI", 11))
        self.chat_area.pack()

        # Entry
        self.entry = tk.Entry(self.window, width=50, bd=0, relief='flat', font=("Segoe UI", 11))
        self.entry.pack(side=tk.LEFT, padx=(10, 0), pady=(0, 10))
        self.entry.bind("<Return>", self.send_message)

        # Buttons style dictionary for reuse
        button_style = {
            'bd': 0,
            'relief': 'flat',
            'font': ("Segoe UI", 10, "bold"),
            'activebackground': '#005f99'
        }

        self.send_button = tk.Button(self.window, text="Send", command=self.send_message,
                                     bg="#007acc", fg="white", **button_style)
        self.send_button.pack(side=tk.LEFT, padx=10, pady=(0, 10))

        self.clear_button = tk.Button(self.window, text="Clear", command=self.clear_chat,
                                      bg="red", fg="white", activebackground="#cc0000",
                                      bd=0, relief='flat', font=("Segoe UI", 10, "bold"))
        self.clear_button.pack(side=tk.LEFT, padx=(0, 10), pady=(0, 10))

        self.apply_theme()
        self.start_chat()

    def apply_theme(self):
        if self.dark_mode:
            bg_color = "#1e1e1e"
            text_bg = "#2e2e2e"
            text_fg = "#e0e0e0"
            entry_bg = "#333"
            entry_fg = "#fff"
            self.window.configure(bg=bg_color)
            self.chat_frame.configure(bg="#444444")
            self.chat_area.configure(bg=text_bg, fg=text_fg)
            self.entry.configure(bg=entry_bg, fg=entry_fg, insertbackground=entry_fg)
            self.send_button.configure(bg="#007acc", fg="white")
            self.clear_button.configure(bg="red", fg="white")
            self.toggle_button.configure(text="Switch to Light Mode", bg="#444", fg="white")
        else:
            bg_color = "#f0f0f0"
            text_bg = "white"
            text_fg = "black"
            entry_bg = "white"
            entry_fg = "black"
            self.window.configure(bg=bg_color)
            self.chat_frame.configure(bg="#ddd")
            self.chat_area.configure(bg=text_bg, fg=text_fg)
            self.entry.configure(bg=entry_bg, fg=entry_fg, insertbackground=entry_fg)
            self.send_button.configure(bg="#007acc", fg="white")
            self.clear_button.configure(bg="red", fg="white")
            self.toggle_button.configure(text="Switch to Dark Mode", bg="#ddd", fg="black")

    def toggle_theme(self):
        self.dark_mode = not self.dark_mode
        self.apply_theme()

    def start_chat(self):
        starter = random.choice(self.bot.random_questions)
        self.display_message(starter, sender="bot")
        self.window.after(100, lambda: self.speak(starter))

    def display_message(self, message, sender="bot"):
        timestamp = datetime.datetime.now().strftime("%H:%M")
        self.chat_area.config(state='normal')

        if sender == "user":
            self.chat_area.insert(tk.END, f"You: {message} ({timestamp})\n\n")
        else:
            self.chat_area.insert(tk.END, f"RuleBot: ", ("bot_label",))
            self.chat_area.insert(tk.END, f"{message} ({timestamp})\n\n", ("bot_message",))

        self.chat_area.config(state='disabled')
        self.chat_area.yview(tk.END)

        self.chat_area.tag_config("bot_message", foreground="orange" if self.dark_mode else "darkblue",
                                  font=("Segoe UI", 11, "italic" if self.dark_mode else "normal"))
        self.chat_area.tag_config("bot_label", foreground="#00ffff", font=("Segoe UI", 11, "bold"))

    def send_message(self, event=None):
        user_msg = self.entry.get().strip()
        if not user_msg:
            return

        self.display_message(user_msg, sender="user")
        self.entry.delete(0, tk.END)

        if user_msg.lower() in self.bot.exit_commands:
            goodbye_msg = "Okay, have a nice Earth day! Goodbye!"
            self.display_message(goodbye_msg, sender="bot")
            self.window.after(100, lambda: self.speak(goodbye_msg))
            self.window.after(2000, self.window.destroy)
            return

        self.display_message("RuleBot is typing...", sender="bot")
        self.window.after(1500, lambda: self.show_bot_reply(user_msg))

    def show_bot_reply(self, user_msg):
        self.chat_area.config(state='normal')
        self.chat_area.delete("end-3l", "end-1l")  # Remove 'typing...' message
        self.chat_area.config(state='disabled')

        bot_reply = self.bot.match_reply(user_msg)
        self.display_message(bot_reply, sender="bot")
        self.window.after(100, lambda: self.speak(bot_reply))

    def clear_chat(self):
        self.chat_area.config(state='normal')
        self.chat_area.delete(1.0, tk.END)
        self.chat_area.config(state='disabled')

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()


if __name__ == "__main__":
    bot = RuleBot()
    gui = ChatGUI(bot)
    gui.window.mainloop()
