import telebot
from telebot import types
#import data_class as dat

token = "5760239776:AAFSum_k7pm7GbC_no4aIZRIGTQiXVLswGc"
bot=telebot.TeleBot(token)
myID1 = 582338838
myID = 1737599584
stud_id_list = []
dz = False
def ch():
    global dz
    dz = False
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,'Привет, напиши /reg Имя Фамилия')


@bot.message_handler(commands=['setdz'])
def start_message(message):
    if message.from_user.id == myID or myID1:
        dzt = message.text[7:]


    else:
        bot.send_message(message.chat.id, 'У вас нет прав на использование этой команды')


@bot.message_handler(commands=['setphdz'])
def start_message(message):
    global dz
    if message.from_user.id == myID or myID1:
        bot.send_message(message.chat.id, 'Отправьте фотографию')
        dz = True
    else:
        bot.send_message(message.chat.id, 'У вас нет прав на использование этой команды')


@bot.message_handler(commands=['reg'])
def start_message(message):
    name = message.text[5:]
    cur_id = message.from_user.id
    if cur_id not in stud_id_list:
        bot.send_message(message.chat.id, 'Ваша заявка отправленна на рассмотрение, ожидайте!')
        bot.send_message(myID, f"Пришла новая заявка на регистрацию от {name} с айди {cur_id}")
    else:
        bot.send_message(message.chat.id, "Вы уже подали заявку на регистрацию")

@bot.message_handler(content_types=['photo'])
def photo(message):
    global dz
    if dz:
         fileID = message.photo[-1].file_id
         file_info = bot.get_file(fileID)
         downloaded_file = bot.download_file(file_info.file_path)
         with open("image.jpg", 'wb') as new_file:
             new_file.write(downloaded_file)
#aoaoa

#mvkrmeovnmofek
bot.infinity_polling()