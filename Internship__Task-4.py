from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a chatbot
bot = ChatBot("My Chatbot")

# Train the chatbot
trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")

print("Chatbot: Hello! I am your chatbot.")
print("Chatbot: Type 'exit' to stop the conversation.")

# Start conversation
while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Chatbot: Goodbye! Have a nice day!")
        break

    response = bot.get_response(user_input)
    print("Chatbot:", response)
