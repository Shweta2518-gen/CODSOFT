import re
import random
from datetime import datetime

GREETINGS = ["Hello! How can I help you today?",
             "Hey there! What's on your mind?",
             "Hi! Great to see you. What can I do for you?"]

FAREWELLS  = ["Goodbye! Have a wonderful day!",
              "See you later! Take care!",
              "Bye! Feel free to chat anytime."]

THANKS     = ["You're welcome!", "Happy to help!", "Anytime!"]

CONFUSED   = ["I'm not sure I understand. Could you rephrase that?",
              "Hmm, I didn't quite catch that. Try asking differently?",
              "I don't have an answer for that yet. Ask me something else!"]

def handle_time(_match):
    now = datetime.now()
    return f"The current time is {now.strftime('%I:%M %p')}."

def handle_date(_match):
    now = datetime.now()
    return f"Today is {now.strftime('%A, %B %d, %Y')}."

def handle_name(_match):
    return "I'm RuBot — a simple rule-based chatbot built in Python!"

def handle_age(_match):
    return "I don't have an age; I was just created moments ago in your terminal!"

def handle_weather(_match):
    return ("I can't check live weather yet, but you could visit "
            "https://weather.com for a forecast!")

def handle_joke(_match):
    jokes = [
        "Why do programmers prefer dark mode?\n  Because light attracts bugs! 🐛",
        "Why did the Python developer wear glasses?\n  Because they couldn't C! 👓",
        "A SQL query walks into a bar, walks up to two tables and asks...\n  'Can I join you?' 😄",
    ]
    return random.choice(jokes)

def handle_help(_match):
    return (
        "Here are things you can ask me:\n"
        "  • Greetings      — say hi, hello, hey\n"
        "  • Time / Date    — 'what time is it?' / 'what's today's date?'\n"
        "  • My identity    — 'what's your name?' / 'who are you?'\n"
        "  • Jokes          — 'tell me a joke'\n"
        "  • Weather        — 'what's the weather?'\n"
        "  • Math           — 'calculate 12 * 7'\n"
        "  • Farewells      — bye, exit, quit\n"
        "  • Type 'help'    — to see this list again"
    )

def handle_math(match):
    """Safely evaluate simple arithmetic expressions."""
    expr = match.group(1).strip()
    # Allow only digits and basic operators
    if re.fullmatch(r"[\d\s\+\-\*/\.\(\)]+", expr):
        try:
            result = eval(expr)          # safe — only numbers & operators pass
            return f"The answer is: {result}"
        except ZeroDivisionError:
            return "Oops! You can't divide by zero."
        except Exception:
            return "I couldn't calculate that. Please check your expression."
    return "I can only handle basic arithmetic (+ - * /)."

def handle_mood(match):
    sentiment = match.group(1).lower()
    positive = {"good", "great", "awesome", "fantastic", "happy", "well",
                "wonderful", "fine", "excellent", "amazing"}
    if sentiment in positive:
        return "That's great to hear! 😊 How can I help you today?"
    return "I'm sorry to hear that. I hope things look up soon! 💙"

RULES = [
    # Greetings
    (re.compile(r"\b(hi|hello|hey|howdy|greetings|good\s?(morning|afternoon|evening))\b", re.I),
     lambda _: random.choice(GREETINGS)),

    # Farewells
    (re.compile(r"\b(bye|goodbye|see\s?you|farewell|exit|quit|cya)\b", re.I),
     lambda _: ("FAREWELL", random.choice(FAREWELLS))),   # special tuple → triggers exit

    # Thank you
    (re.compile(r"\b(thanks|thank\s?you|thx|ty)\b", re.I),
     lambda _: random.choice(THANKS)),

    # Help
    (re.compile(r"\bhelp\b", re.I), handle_help),

    # Time
    (re.compile(r"\b(what('?s| is) the time|current time|time now|what time)\b", re.I),
     handle_time),

    # Date
    (re.compile(r"\b(what('?s| is) (today('?s)?|the) date|today('?s)? date|what day)\b", re.I),
     handle_date),

    # Bot identity
    (re.compile(r"\b(what('?s| is) your name|who are you|your name|are you a bot|are you human)\b", re.I),
     handle_name),

    # Bot age
    (re.compile(r"\b(how old are you|your age)\b", re.I), handle_age),

    # Weather
    (re.compile(r"\b(weather|forecast|temperature outside)\b", re.I), handle_weather),

    # Joke
    (re.compile(r"\b(joke|tell me something funny|make me laugh|funny)\b", re.I), handle_joke),

    # Calculator  —  "calculate 3 + 4" or "what is 100 / 5"
    (re.compile(r"(?:calculate|compute|what(?:'?s| is))\s+([\d\s\+\-\*/\.\(\)]+)", re.I),
     handle_math),

    # Mood  —  "I am feeling great"
    (re.compile(r"\b(?:i(?:'?m| am)|feeling)\s+(\w+)\b", re.I), handle_mood),
]
def get_response(user_input: str):
    """
    Iterate through RULES; return the first matching response.
    Returns a tuple (response_text, should_exit).
    """
    text = user_input.strip()

    for pattern, handler in RULES:
        match = pattern.search(text)
        if match:
            result = handler(match)
            # Check for farewell sentinel
            if isinstance(result, tuple) and result[0] == "FAREWELL":
                return result[1], True
            return result, False

    return random.choice(CONFUSED), False

def main():
    print("=" * 55)
    print("  Welcome to RuBot — Your Rule-Based Python Chatbot!")
    print("  Type 'help' to see what I can do.")
    print("  Type 'bye' or 'quit' to exit.")
    print("=" * 55)

    while True:
        try:
            user_input = input("\nYou: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nRuBot: Goodbye! Have a great day!")
            break

        if not user_input:
            print("RuBot: Please type something — I'm listening!")
            continue

        response, should_exit = get_response(user_input)
        print(f"\nRuBot: {response}")

        if should_exit:
            break

    print("\n" + "=" * 55)


if __name__ == "__main__":
    main()