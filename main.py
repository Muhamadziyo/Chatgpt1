import telebot
import openai

# OpenAI GPT-3 API kalitingizni sozlang
openai.api_key = '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'

#Telegram bot tokeningizni o'rnating
TELEGRAM_BOT_TOKEN = '6352084344:AAFVzp9go32vAs-FbGXqlewKdn2b9h649V4'

# Botni ishga tushiring
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)
88
# Boshlash buyrug'i ishlovchisini aniqlang
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message, "Hi! I am your ChatGPT 3.5 bot🤖. Send me a message, and I will respond.")

# Xabar ishlov beruvchisini aniqlang7
@bot.message_handler(func=lambda message: True)

def handle_message(message):
    user_input = message.text
    bot_response = chat_with_gpt3(user_input)
    bot.reply_to(message, f"ChatGPT🤖: {bot_response}")

#GPT-3 bilan suhbatlashish funksiyasini aniqlang
def chat_with_gpt3(prompt):
    
    prompt = f'User: {prompt}\nChatGPT:'
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        temperature=0.7,
        
    )
    return response.choices[0].text.strip()

#  Botningishlashini ta'minlash uchun ovoz berish davri
bot.polling()

