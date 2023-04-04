import telebot
import os
from telebot import types
#import data_class as dat
import data_class
dztt = False
token = "5760239776:AAFSum_k7pm7GbC_no4aIZRIGTQiXVLswGc"
bot=telebot.TeleBot(token)
myID1 = 582338838
myID = 1737599584
stud_id_list = []
dz = False
data = data_class.StudentsData()
stud = []
a = ""
name123 = 123
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,'Привет, напиши /reg Имя Фамилия')
def allstud():
    global a
    for i in data.getAllStudens():
        stud.append(i[0])
    a = ", ".join(stud)

    return a

@bot.message_handler(commands=['getdz'])
def start_message(message):
    if data.getDz(message.chat.id) == "Фото":
        bot.send_photo(message.chat.id, photo=open(f"{message.chat.id}.jpg", "rb"))
    else:
        bot.send_message(message.chat.id, data.getDz(message.chat.id))
        data.getDz(message.chat.id)

@bot.message_handler(commands=['setdz'])
def start_message(message):
    if message.from_user.id == myID or myID1:
        dz = message.text[7:]
        name = dz[0:dz.find(" ")]
        dz = dz[dz.find(" ")+1:]
        data.setDz(data.getStudId(name),dz)
    else:
        bot.send_message(message.chat.id, 'У вас нет прав на использование этой команды')

@bot.message_handler(commands=['all'])
def start_message(message):
    if message.from_user.id == myID or myID1:
        bot.send_message(message.chat.id, allstud())


@bot.message_handler(commands=['setphdz'])
def start_message(message):
    global dz
    if message.from_user.id == myID or message.from_user.id == myID1:
        global name123
        name123 = message.text[9:]
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
        data.newStudent(cur_id, name)
        bot.send_message(myID, f"Пришла новая заявка на регистрацию от {name} с айди {cur_id}")
    else:
        bot.send_message(message.chat.id, "Вы уже подали заявку на регистрацию")




@bot.message_handler(content_types=['photo'])
def photo(message):
    global dz
    if dz and message.from_user.id == myID:
        fileID = message.photo[-1].file_id
        file_info = bot.get_file(fileID)
        downloaded_file = bot.download_file(file_info.file_path)
        with open(rf"{data.getStudId(name123)}.jpg", 'wb') as new_file:
            new_file.write(downloaded_file)
            data.setDz(data.getStudId(name123),"Фото")
        bot.send_message(message.chat.id, "Дз задано!")
    dz = False




bot.infinity_polling()