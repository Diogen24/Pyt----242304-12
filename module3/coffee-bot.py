import telebot
import requests

from bot_token import TOKEN

bot=telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['coffee'])
def send_coffee(message):
    coffee=requests.get('https://coffee.alexflipnote.dev/random.json').json()
    image=coffee['file']
    bot.send_photo(message.chat.id,image)
    
if __name__=='__main__':
    bot.infinity_polling()