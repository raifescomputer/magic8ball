import random

responses = [
    "I don't think so, girl.",
    "Outlook hazy, try asking your therapist.",
    "Reply hazy, ask again after I've had coffee.",
    "Don't count on it, unless you're feeling lucky... punk.",
    "As I see it, yeah... but I've been wrong before. (Rarely.)",
    "It is decidedly so... if you're into that sort of thing.",
    "Without a doubt... probably. Unless something goes horribly wrong.",
    "Signs point to yes... but I'm just a ball, what do I know?",
    "Concentrate and ask again... if you dare.",
    "My reply is no... but feel free to ignore me.",
    "Outlook not so good... for you, anyway.",
    "Very doubtful... like your chances of winning the lottery.",
    "In your dreams, maybe. Now go bother someone else.",
    "You're kidding, right? Seriously?"

]

question = input("Ask me anything... if you're brave... ")

response = random.choice(responses)

print(response + '♥') 