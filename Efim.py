import telebot
from telebot import types
myid =582338838
stud_list=[]
bot=telebot.TeleBot()
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
