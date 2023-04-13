import telebot
from telebot import types
myid =582338838
stud_list=[]
bot=telebot.TeleBot("5760239776:AAFSum_k7pm7GbC_no4aIZRIGTQiXVLswGc")
'''
@bot.message_handler(content_types=["text"])
def message_reply(message):
    if menuOpen:
        if message.chat.id in stud_id_list:
            if message.text=="Узнать homeWork":
                dz=data.getDz(message.chat.id)
                if dz == "фото":
                    photo=open(f"{message.chat.id}.jpg","rb")
                    bot.send_photo(message.chat.id,photo)

                else:
                    bot.send_message(message.chat.id,f"DOMASHKA FOR YOU: {dz}")
            if message.text == "КОГДА УРОК А МОЖЕТ Я ОПОЗДАЛ???":
                nlinfo=data.getNextLsn(message.chat.id)
                bot.send_message(message.chat.id,text=f'Следущее занятие: {nlinfo}')
        else:
            bot.send_message(message.chat.id,text="Ты не зарегался или ты не мой ученик😭.")
'''
@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.InlineKeyboardMarkup()
    button = telebot.types.InlineKeyboardButton(text='CLick me', callback_data='add')
    markup.add(button)
    bot.send_message(chat_id=message.chat.id, text='Some text', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    if call.data == 'add':
        bot.answer_callback_query(callback_query_id=call.id, text='Hello world')





bot.infinity_polling()