import telebot
from bot_token import TOKEN

bot=telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text'])
def create_poll(message):
    if 1<message.text.count('\n')<11:
        strings=message.text.split('\n')
        question=strings[0]
        answers=strings[1:]
        bot.send_poll(message.chat.id, question, answers)
    else:
        bot.send_message(message.chat.id, f'В вашем сообщении должно быть от 3 до 11 строк')
    
if __name__=='__main__':
    bot.infinity_polling()