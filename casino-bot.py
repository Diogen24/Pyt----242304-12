import telebot
import random
from bot_token import TOKEN

bot=telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    keyboard=telebot.types.InlineKeyboardMarkup()
    list=[]
    for i in range(5):
        list.append(telebot.types.InlineKeyboardButton(text='0', callback_data=str(i)))
    keyboard.row(*list)
    bot.send_message(message.chat.id, 'choose', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call:True)
def callback_query(call):
    if random.randint(0,4)==int(call.data):
        bot.send_message(call.message.chat.id, 'victory')
    else:
        bot.send_message(call.message.chat.id, 'lose')

if __name__=='__main__':
    bot.infinity_polling()