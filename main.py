import telebot
import os
from telebot import types
import data_class
dztt = False
myID = 1737599584
myID1 = 582338838
combine = []
token = "5760239776:AAFSum_k7pm7GbC_no4aIZRIGTQiXVLswGc"
bot=telebot.TeleBot(token)
stud_id_list = [582338838]
par_id_list = []
teach_id = [1737599584]
dz = False
data = data_class.StudentsData()
stud = []
a = ""
curStud = None
phrases = ['Ты уже зарегистрирован!', "Эта комманда бесполезна для тебя","Вы сломали бота поздравляю","А нет мне показалось)))","ТЫ СЕРЬЁЗНО ВСЁ ЕЩЁ ТЫКАЕШЬ СТАРТ","Ну прекрати","Если ты ещё раз тыкнешь старт,то к дз прибавится 1 задание","А ты любишь риск","Ладно ты победил(ла) , можешь не делать дз","Ну это ряльно конец.","P.S сделали Миша,Ефим,Макс","Макс не очень работал над фразами."]
def check_perm(id):
    if id in stud_id_list:
        return 1
    elif id in par_id_list:
        return 2
    elif id in teach_id:
        return 3
    else:
        return 0

def replace_id(cur_id):
    for item in combine:
        if item[0] == cur_id:
            return item[1]

@bot.message_handler(commands=['start'])
def start_message(message):
    if check_perm(message.chat.id) == 0:
        bot.send_message(message.chat.id,'Привет, напиши /reg Имя Фамилия')
    elif check_perm(message.chat.id) == 1:
        x=data.getStartCount(message.chat.id)
        bot.send_message(message.chat.id,phrases[x])
        data.setStartCount(message.chat.id)
    elif check_perm(message.chat.id) == 2:
        bot.send_message(message.chat.id,'')




@bot.message_handler(commands=['getdz'])
def start_message(message):
    if check_perm(message.chat.id) == 3:
        name = message.text[7:]
        if data.getDz(message.chat.id) == "Фото":
            bot.send_photo(message.chat.id, photo=open(f"data/{data.getStudId(name)}.jpg", "rb"))
        else:
            bot.send_message(message.chat.id, data.getDz(message.chat.id))
    elif check_perm(message.chat.id) == 2:
        print(1)

@bot.message_handler(commands=['setdz'])
def start_message(message):
    if check_perm(message.from_user.id) == 3:
        dz = message.text[7:]
        name = dz[0:dz.find(" ")]
        dz = dz[dz.find(" ")+1:]
        data.setDz(data.getStudId(name),dz)
    else:
        bot.send_message(message.chat.id, 'У вас нет прав на использование этой команды')

@bot.message_handler(commands=['all'])
def start_message(message):
    if check_perm(message.from_user.id) == 3:
        stud = []
        for i in data.getAllStudens():
            stud.append(i)
        a = ", ".join(stud)
        bot.send_message(message.chat.id, a)


@bot.message_handler(commands=['setphdz'])
def start_message(message):
    global dz
    global curStud
    if check_perm(message.from_user.id) == 3:
        curStud = message.text[9:]
        bot.send_message(message.chat.id, 'Отправьте фотографию')
        dz = True


@bot.message_handler(commands=['reg'])
def start_message(message):
    name = message.text[5:]
    cur_id = message.from_user.id
    if cur_id not in stud_id_list:
        bot.send_message(message.chat.id, 'Ваша заявка отправленна на рассмотрение, ожидайте!')
        bot.send_message(myID, f"Пришла новая заявка на регистрацию от {name} с айди {cur_id}")
    else:
        bot.send_message(message.chat.id, "Вы уже подали заявку на регистрацию")


@bot.message_handler(commands=['getparname'])
def start_message(message):
    if check_perm(message.from_user.id) == 3:
        nm = message.text[12:]
        bot.send_message(message.chat.id, data.getParName(data.getStudId(nm)))
    else:
        bot.send_message(message.chat.id, 'У вас нет прав на использование этой команды')


@bot.message_handler(commands=['getparnum'])
def start_message(message):
    if check_perm(message.from_user.id) == 3:
        nm = message.text[11:]

        bot.send_message(message.chat.id, data.getParNum(data.getStudId(nm)))
    else:
        bot.send_message(message.chat.id, 'У вас нет прав на использование этой команды')


@bot.message_handler(commands=['getstudnum'])
def start_message(message):
    if check_perm(message.from_user.id) == 3:
        nm = message.text[12:]

        bot.send_message(message.chat.id, data.getStudNum(data.getStudId(nm)))
    else:
        bot.send_message(message.chat.id, 'У вас нет прав на использование этой команды')


@bot.message_handler(commands=['getnextlsn'])
def start_message(message):
    if check_perm(message.from_user.id) == 3:
        nm = message.text[12:]
        bot.send_message(message.chat.id, data.getNextLsn(data.getStudId(nm)))
    elif check_perm(message.from_user.id) == 1:
        bot.send_message(message.chat.id, data.getNextLsn(message.from_user.id))
    elif check_perm(message.chat.id) == 2:
        bot.send_message(message.chat.id, data.getNextLsn(replace_id(message.chat.id)))
    else:
        bot.send_message(message.chat.id, 'У вас нет прав на использование этой команды')



@bot.message_handler(commands=['getlastheme'])
def start_message(message):
    if check_perm(message.from_user.id) == 3:
        nm = message.text[13:]
        bot.send_message(message.chat.id, data.getLastTheme(data.getStudId(nm)))
    elif check_perm(message.from_user.id) == 1:
        bot.send_message(message.chat.id, data.getLastTheme(message.from_user.id))
    elif check_perm(message.from_user.id) == 2:
        bot.send_message(message.chat.id, data.getLastTheme(replace_id(message.chat.id)))
    else:
        bot.send_message(message.chat.id, 'У вас нет прав на использование этой команды')



@bot.message_handler(commands=['getpaid'])
def start_message(message):
    if check_perm(message.from_user.id) == 3:
        nm = message.text[9:]
        bot.send_message(message.chat.id, data.getPaid(data.getStudId(nm)))
    elif check_perm(message.from_user.id) == 2:
        bot.send_message(message.chat.id, data.getPaid(replace_id(message.chat.id)))
    else:
        bot.send_message(message.chat.id, 'У вас нет прав на использование этой команды')


@bot.message_handler(commands=['getlessons'])
def start_message(message):
    if check_perm(message.from_user.id) == 3:
        nm = message.text[12:]
        bot.send_message(message.chat.id, data.getLessons(data.getStudId(nm)))
    elif check_perm(message.from_user.id) == 2:
        bot.send_message(message.chat.id, data.getLessons(replace_id(message.chat.id)))
    else:
        bot.send_message(message.chat.id, 'У вас нет прав на использование этой команды')

@bot.message_handler(commands=['getstudname'])
def start_message(message):
    if check_perm(message.from_user.id) == 3:
        nm = message.text[13:]
        bot.send_message(message.chat.id, data.getStudName(int(nm)))
    else:
        bot.send_message(message.chat.id, 'У вас нет прав на использование этой команды')

@bot.message_handler(commands=['getstudid'])
def start_message(message):
    if check_perm(message.from_user.id) == 3:
        nm = message.text[11:]
        bot.send_message(message.chat.id, data.getStudId(nm))
    else:
        bot.send_message(message.chat.id, 'У вас нет прав на использование этой команды')


@bot.message_handler(commands=['setparname'])
def start_message(message):
    if check_perm(message.from_user.id) == 3:
        nm = message.text[12:]
        idd = nm[0:nm.find(" ")]
        nm = nm[nm.find(" ") + 1:]
        data.setParName(data.getStudId(idd), nm)
        bot.send_message(message.chat.id, "Имя родителя изменено")
    else:
        bot.send_message(message.chat.id, 'У вас нет прав на использование этой команды')

@bot.message_handler(commands=['setparnum'])
def start_message(message):
    if check_perm(message.from_user.id) == 3:
        idd = message.text[11:]
        nm = idd[0:idd.find(" ")]
        idd = idd[idd.find(" ") + 1:]
        data.setParNum(data.getStudId(nm), idd)
        bot.send_message(message.chat.id, "Телефон родителя изменен")
    else:
        bot.send_message(message.chat.id, 'У вас нет прав на использование этой команды')




@bot.message_handler(commands=['setstudnum'])
def start_message(message):
    if check_perm(message.from_user.id) == 3:
        idd = message.text[12:]
        nm = idd[0:idd.find(" ")]
        idd = idd[idd.find(" ") + 1:]
        data.setStudNum(data.getStudId(nm), idd)
        bot.send_message(message.chat.id, "Телефон ученика изменен")
    else:
        bot.send_message(message.chat.id, 'У вас нет прав на использование этой команды')


@bot.message_handler(commands=['setnextlsn'])
def start_message(message):
    if check_perm(message.from_user.id) == 3:
        idd = message.text[12:]
        nm = idd[0:idd.find(" ")]
        idd = idd[idd.find(" ") + 1:]
        data.setNextLsn(data.getStudId(nm), idd)
        bot.send_message(message.chat.id, "Дата следуюшего урока изменена")
    else:
        bot.send_message(message.chat.id, 'У вас нет прав на использование этой команды')




@bot.message_handler(commands=['setlasttheme'])
def start_message(message):
    if check_perm(message.from_user.id) == 3:
        idd = message.text[14:]
        nm = idd[0:idd.find(" ")]
        idd = idd[idd.find(" ") + 1:]
        data.setLastTheme(data.getStudId(nm), idd)
        bot.send_message(message.chat.id, "Последняя тема изменена")
    else:
        bot.send_message(message.chat.id, 'У вас нет прав на использование этой команды')


@bot.message_handler(commands=['setpaid'])
def start_message(message):
    if check_perm(message.from_user.id) == 3:
        idd = message.text[9:]
        nm = idd[0:idd.find(" ")]
        idd = idd[idd.find(" ") + 1:]
        data.setPaid(data.getStudId(nm), idd)
        bot.send_message(message.chat.id, "Кол-во оплаченых занятий изменено")
    else:
        bot.send_message(message.chat.id, 'У вас нет прав на использование этой команды')


@bot.message_handler(commands=['setlessons'])
def start_message(message):
    if check_perm(message.from_user.id) == 3:
        idd = message.text[12:]
        nm = idd[0:idd.find(" ")]
        idd = idd[idd.find(" ") + 1:]
        data.setLessons(data.getStudId(nm), idd)
        bot.send_message(message.chat.id, "Кол-во прошедших занятий изменено")
    else:
        bot.send_message(message.chat.id, 'У вас нет прав на использование этой команды')


@bot.message_handler(commands=['setstudname'])
def start_message(message):
    if check_perm(message.from_user.id) == 3:
        idd = message.text[13:]
        nm = idd[0:idd.find(" ")]
        idd = idd[idd.find(" ") + 1:]
        data.setStudName(data.getStudId(nm), idd)
        bot.send_message(message.chat.id, "Имя ученика изменено")
    else:
        bot.send_message(message.chat.id, 'У вас нет прав на использование этой команды')


@bot.message_handler(commands=['newstudent'])
def start_message(message):
    if check_perm(message.from_user.id) == 3:
        fspace = message.text.find(" ")
        lspace = message.text.rfind(" ")
        name = message.text[fspace+1:lspace]
        cur_id = message.text[lspace:]
        stud_id_list.append(cur_id)
        data.newStudent(cur_id, name)
        bot.send_message(message.chat.id, "Ученик добавлен")
    else:
        bot.send_message(message.chat.id, 'У вас нет прав на использование этой команды')




@bot.message_handler(commands=['delstud'])
def start_message(message):
    if check_perm(message.from_user.id) == 3:
        nm = message.text[9:]
        print(nm)
        try:
            data.delStud(nm)
            bot.send_message(message.chat.id, "Ученик удален")
        except:
            bot.send_message(message.chat.id, "Нет такого")
    else:
        bot.send_message(message.chat.id, 'У вас нет прав на использование этой команды')
@bot.message_handler(content_types=['photo'])
def photo(message):
    global dz
    if dz and check_perm(message.from_user.id) == 3:
        fileID = message.photo[-1].file_id
        file_info = bot.get_file(fileID)
        downloaded_file = bot.download_file(file_info.file_path)
        with open(rf"data/{data.getStudId(curStud)}.jpg", 'wb') as new_file:
            new_file.write(downloaded_file)
            data.setDz(data.getStudId(curStud),"Фото")
        bot.send_message(message.chat.id, "Дз задано!")
    dz = False



















bot.infinity_polling()