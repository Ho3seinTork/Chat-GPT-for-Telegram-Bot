import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import telebot
from openai import OpenAI

# Replace with your own values
TELEGRAM_TOKEN = ''  # Your Telegram bot token
OPENAI_API_KEY = ''  # Your OpenAI API key

bot = telebot.TeleBot(TELEGRAM_TOKEN)
client = OpenAI(api_key=OPENAI_API_KEY)

# System prompt to control model behavior
SYSTEM_PROMPT = """ """

# Function to communicate with OpenAI GPT-4 language model
def call_language_model(prompt):
    response = client.chat.completions.create(
        model="gpt-4o", 
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},  # System prompt
            {"role": "user", "content": prompt}  # User message
        ]
    )
    return response.choices[0].message.content.strip()

# Handler for /start command
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, "Hello! I'm a Telegram bot powered by OpenAI's GPT-4 language model. How can I help you?")

# Handler for text messages
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_message = message.text
    response = call_language_model(user_message)
    bot.reply_to(message, response)

# Start the bot
print("Bot is running...")
bot.polling()
