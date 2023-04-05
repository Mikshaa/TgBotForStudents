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




@bot.message_handler(commands=['getparname'])
def start_message(message):
    if message.from_user.id == myID or message.from_user.id == myID1:
        nm = message.text[12:]
        bot.send_message(message.chat.id, data.getParName(data.getStudId(nm)))
    else:
        bot.send_message(message.chat.id, 'У вас нет прав на использование этой команды')


@bot.message_handler(commands=['getparnum'])
def start_message(message):
    if message.from_user.id == myID or message.from_user.id == myID1:
        nm = message.text[11:]

        bot.send_message(message.chat.id, data.getParNum(data.getStudId(nm)))
    else:
        bot.send_message(message.chat.id, 'У вас нет прав на использование этой команды')


@bot.message_handler(commands=['getstudnum'])
def start_message(message):
    if message.from_user.id == myID or message.from_user.id == myID1:
        nm = message.text[12:]

        bot.send_message(message.chat.id, data.getStudNum(data.getStudId(nm)))
    else:
        bot.send_message(message.chat.id, 'У вас нет прав на использование этой команды')


@bot.message_handler(commands=['getnextlsn'])
def start_message(message):
    if message.from_user.id == myID or message.from_user.id == myID1:
        nm = message.text[12:]
        bot.send_message(message.chat.id, data.getNextLsn(data.getStudId(nm)))
    else:
        bot.send_message(message.chat.id, 'У вас нет прав на использование этой команды')



@bot.message_handler(commands=['getlastheme'])
def start_message(message):
    if message.from_user.id == myID or message.from_user.id == myID1:
        nm = message.text[13:]
        bot.send_message(message.chat.id, data.getLastTheme(data.getStudId(nm)))
    else:
        bot.send_message(message.chat.id, 'У вас нет прав на использование этой команды')



@bot.message_handler(commands=['getpaid'])
def start_message(message):
    if message.from_user.id == myID or message.from_user.id == myID1:
        nm = message.text[9:]
        bot.send_message(message.chat.id, data.getPaid(data.getStudId(nm)))
    else:
        bot.send_message(message.chat.id, 'У вас нет прав на использование этой команды')


@bot.message_handler(commands=['getlessons'])
def start_message(message):
    if message.from_user.id == myID or message.from_user.id == myID1:
        nm = message.text[12:]
        bot.send_message(message.chat.id, data.getLessons(data.getStudId(nm)))
    else:
        bot.send_message(message.chat.id, 'У вас нет прав на использование этой команды')

@bot.message_handler(commands=['getstudname'])
def start_message(message):
    if message.from_user.id == myID or message.from_user.id == myID1:
        nm = message.text[13:]
        bot.send_message(message.chat.id, data.getStudName(int(nm)))
    else:
        bot.send_message(message.chat.id, 'У вас нет прав на использование этой команды')

@bot.message_handler(commands=['getstudid'])
def start_message(message):
    if message.from_user.id == myID or message.from_user.id == myID1:
        nm = message.text[11:]
        bot.send_message(message.chat.id, data.getStudId(nm))
    else:
        bot.send_message(message.chat.id, 'У вас нет прав на использование этой команды')


@bot.message_handler(commands=['setparname'])
def start_message(message):
    if message.from_user.id == myID or message.from_user.id == myID1:
        nm = message.text[12:]
        idd = nm[0:nm.find(" ")]
        nm = nm[nm.find(" ") + 1:]
        data.setParName(data.getStudId(idd), nm)
        bot.send_message(message.chat.id, "Имя родителя изменено")
    else:
        bot.send_message(message.chat.id, 'У вас нет прав на использование этой команды')

@bot.message_handler(commands=['setparnum'])
def start_message(message):
    if message.from_user.id == myID or message.from_user.id == myID1:
        idd = message.text[11:]
        nm = idd[0:idd.find(" ")]
        idd = idd[idd.find(" ") + 1:]
        data.setParNum(data.getStudId(nm), idd)
        bot.send_message(message.chat.id, "Телефон родителя изменен")
    else:
        bot.send_message(message.chat.id, 'У вас нет прав на использование этой команды')




@bot.message_handler(commands=['setstudnum'])
def start_message(message):
    if message.from_user.id == myID or message.from_user.id == myID1:
        idd = message.text[12:]
        nm = idd[0:idd.find(" ")]
        idd = idd[idd.find(" ") + 1:]
        data.setStudNum(data.getStudId(nm), idd)
        bot.send_message(message.chat.id, "Телефон ученика изменен")
    else:
        bot.send_message(message.chat.id, 'У вас нет прав на использование этой команды')


@bot.message_handler(commands=['setnextlsn'])
def start_message(message):
    if message.from_user.id == myID or message.from_user.id == myID1:
        idd = message.text[12:]
        nm = idd[0:idd.find(" ")]
        idd = idd[idd.find(" ") + 1:]
        data.setNextLsn(data.getStudId(nm), idd)
        bot.send_message(message.chat.id, "Дата следуюшего урока изменена")
    else:
        bot.send_message(message.chat.id, 'У вас нет прав на использование этой команды')




@bot.message_handler(commands=['setlasttheme'])
def start_message(message):
    if message.from_user.id == myID or message.from_user.id == myID1:
        idd = message.text[14:]
        nm = idd[0:idd.find(" ")]
        idd = idd[idd.find(" ") + 1:]
        data.setLastTheme(data.getStudId(nm), idd)
        bot.send_message(message.chat.id, "Последняя тема изменена")
    else:
        bot.send_message(message.chat.id, 'У вас нет прав на использование этой команды')


@bot.message_handler(commands=['setpaid'])
def start_message(message):
    if message.from_user.id == myID or message.from_user.id == myID1:
        idd = message.text[9:]
        nm = idd[0:idd.find(" ")]
        idd = idd[idd.find(" ") + 1:]
        print(idd,nm)
        data.setPaid(data.getStudId(nm), idd)
        bot.send_message(message.chat.id, "Кол-во оплаченых занятий изменено")
    else:
        bot.send_message(message.chat.id, 'У вас нет прав на использование этой команды')


@bot.message_handler(commands=['setlessons'])
def start_message(message):
    if message.from_user.id == myID or message.from_user.id == myID1:
        idd = message.text[12:]
        nm = idd[0:idd.find(" ")]
        idd = idd[idd.find(" ") + 1:]
        data.setLessons(data.getStudId(nm), idd)
        bot.send_message(message.chat.id, "Кол-во прошедших занятий изменено")
    else:
        bot.send_message(message.chat.id, 'У вас нет прав на использование этой команды')


@bot.message_handler(commands=['setstudname'])
def start_message(message):
    if message.from_user.id == myID or message.from_user.id == myID1:
        idd = message.text[13:]
        nm = idd[0:idd.find(" ")]
        idd = idd[idd.find(" ") + 1:]
        data.setStudName(data.getStudId(nm), idd)
        bot.send_message(message.chat.id, "Имя ученика изменено")
    else:
        bot.send_message(message.chat.id, 'У вас нет прав на использование этой команды')


@bot.message_handler(commands=['newstudent'])
def start_message(message):
    if message.from_user.id == myID or message.from_user.id == myID1:
        idd = message.text[12:]
        nm = idd[0:idd.find(" ")]
        idd = idd[idd.find(" ") + 1:]
        data.newStudent(data.getStudId(nm), idd)
        bot.send_message(message.chat.id, "Ученика добавлен")
    else:
        bot.send_message(message.chat.id, 'У вас нет прав на использование этой команды')




@bot.message_handler(commands=['delstud'])
def start_message(message):
    if message.from_user.id == myID or message.from_user.id == myID1:
        nm = message.text[9:]
        data.delStud(data.getStudId(nm))
        bot.send_message(message.chat.id, "Ученик удален")
    else:
        bot.send_message(message.chat.id, 'У вас нет прав на использование этой команды')


























bot.infinity_polling()