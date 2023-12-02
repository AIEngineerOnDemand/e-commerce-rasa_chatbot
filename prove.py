
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chatbot
chatbot = ChatBot('E-commerce ChatBot')

# Train the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

# Define a function to get product recommendations from the mock API
def get_product_recommendations():
    response = requests.get('https://myapi.com/products')
    return response.json()

# Get a response
user_input = "Can you recommend a product?"
if "recommend" in user_input and "product" in user_input:
    products = get_product_recommendations()
    response = f"I recommend {products[0]['name']}"
else:
    response = chatbot.get_response(user_input)

print(response)