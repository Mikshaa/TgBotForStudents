import telebot
from telebot import types
myid =582338838
stud_list=[]
bot=telebot.TeleBot("6134963735:AAHmMiLAxkabV2p38DJky9kEOVxIDb5C2tY")
'''
@bot.message_handler(content_types=["text"])
def message_reply(message):
    if menuOpen:
        if message.chat.id in stud_id_list:
            if message.text=="Узнать homeWork":
                dz=data.getDz(message.chat.id)
                if dz == "Фото":
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
@bot.message_handler(commands=['menu'])
def start(message):
    markup = telebot.types.InlineKeyboardMarkup()
    button = telebot.types.InlineKeyboardButton(text='Домашку скинул быстро!!!!!', callback_data='add')
    button2 = telebot.types.InlineKeyboardButton(text='КОГДА УРОК А МОЖЕТ Я ОПОЗДАЛ???', callback_data='add')
    markup.add(button)
    markup.add(button2)
    bot.send_photo(chat_id=message.chat.id, photo=open("osel.png", "rb"),caption='Самые полезные функции(А может и нет)', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    if call.data == 'add':
        bot.answer_callback_query(callback_query_id=call.id, text='Hello world')
        print(call.id)




@bot.message_handler(commands=['help'])
def helper(message):
    #if check_perm(message.chat.id)==1:
    bot.send_message(message.chat.id,text="ФУНКЦИИ\n"
                                          "/getdz-Получить домашку чтобы не сидеть без дела\n"
                                          "/getnextlesson-Узнать когда следуюшиий урок(чтобы не опоздать)")
bot.infinity_polling()
