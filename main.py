import telebot
from conf import TOKEN

bot=telebot.TeleBot(TOKEN)
@bot.message_handler(commands=["start"])
def handle_start(message):
    bot.send_message(message.chat.id,"Hello!")

@bot.message_handler()
def handle_all(message):
    #bot.reply_to(message,message.text) # Ответ на сообщение с тем же текстом.
    #bot.send_message(message.chat.id,message.text) # Отправить сообщение в тот же чат откуда пришло с тем же текстом.
    #bot.forward_message(message.chat.id,message.chat.id,message.id) # Переслать сообщение в тот же чат откуда пришло сообщение.
    with open("static/image.webp", "rb") as photo:
        bot.send_sticker(message.chat.id, photo, reply_to_message_id=message.message_id) # Отправить стикер в тот же чат откуда пришло сообщение.

bot.infinity_polling()