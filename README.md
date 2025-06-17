# Chatbot-using-Python-NLP-and-Data-Science-
This project is a simple yet powerful AI-based chatbot built using Python, Natural Language Processing (NLP) techniques, and Data Science tools. The chatbot is capable of understanding user input, processing natural language, and responding in a conversational manner.

Project Overview
RuleBot started as a basic rule-based chatbot that responded to user inputs based on predefined patterns. Over time, it was extended with a graphical user interface (GUI) and speech capabilities to make it more interactive and user-friendly.

Development Progress
1. Initial Rule-Based Bot
Implemented a simple Python class that uses regular expressions to match user inputs against known intents.

Supported a few basic patterns such as:

Describing a fictional planet.

Explaining the chatbot's presence on Earth.

Talking about Intellipaat.

Responded with random fallback replies when no intent was matched.

2. GUI Integration with Tkinter
Added a clean and functional GUI using Tkinter.

Included a scrollable chat display area, input text box, and a send button.

Allowed pressing "Enter" to send messages.

Displayed both user and bot messages in the chat area.

3. Exit Handling
Included exit commands like "bye", "quit", "exit" to allow users to end the conversation gracefully.

4. Speech Input and Output
Integrated speech recognition using the speech_recognition library to allow users to speak instead of typing.

Used pyttsx3 for text-to-speech so that the bot could speak its responses aloud.

Added a microphone button in the GUI to capture voice input and convert it into text.

Features
Rule-based intent matching using regular expressions.

Predefined questions and responses.

GUI built using Tkinter.

Speech input using microphone.

Text-to-speech voice output.

Randomized fallback responses.

Exit functionality.

Technologies Used
Python 3

Tkinter for GUI

re for regular expressions

speech_recognition for capturing voice input

pyttsx3 for text-to-speech output

pyaudio for microphone integration

random for selecting fallback replies and starter questions

How to Run
Install the required libraries:

bash
Copy
Edit
pip install speechrecognition pyttsx3 pyaudio
If you face issues with installing pyaudio, use:

bash
Copy
Edit
pip install pipwin
pipwin install pyaudio
Run the script:

bash
Copy
Edit
python Rule-Based-Bot.py
Future Enhancements
Use NLP-based intent classification with libraries like NLTK or spaCy.

Add memory so the bot can remember past interactions.

Enable learning new responses during the conversation.

Add multi-language support.

Allow user-defined intents via external JSON or config files.

License
This project is open for educational and personal use. Contributions and modifications are welcome.

