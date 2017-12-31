import telebot

db_name = "alice.db"

sql_users = """create table Users(
        ID integer,
        Name text,
        Class text,
        Score integer,
        primary key(ID))"""

sql_docs = """create table Docs(
        ID integer,
        Subject text,
        Module integer,
        Department text,
        primary key(ID))"""

sql_remind = """create table Reminders(
        ID integer,
        title text,
        description text,
        class text,
        date text,
        primary key(ID))"""

sql_admins = """create table Admins(
        ID integer,
        primary key(ID))"""

tables = {'Admins': sql_admins, 'Users': sql_users, 'Docs': sql_docs, 'Reminders': sql_remind}


bot = telebot.TeleBot('501737753:AAH_xjdeSe1pUg5cEBazOAFRTaYuqZUzbms') # Bot Token, obtained from @botfather

keyboard_default = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_default.row('/help', '/quote')
keyboard_default.row('/reminders')
keyboard_default.row('/documents')
keyboard_default.row('/whatsmytelegramid')

keyboard_admin = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_admin.row('/help')
keyboard_admin.row('/adddocs', '/addreinders')
keyboard_admin.row('docs', '/reminders')


superuser = [371847809, ]

helpmsg_default = 'Welcome to Alice Bot!\n\nThis is Version 1.0\n\nHere are the cool things that I can do:\n\n\t '+ u'\U0001F514'+' /documents : It will indicate the subject, module and type of document to download onto your phone\n\n\t '+ u'\U0001F514'+' /reminders: It will show the top points to keep in mind for the upcoming sessions at college\n\n\t '+ u'\U0001F514'+' /feedback: It takes a response from the user, regarding the experience interacting with AliceBot. Only 3 responses per day maximum.\n\n\t '+ u'\U0001F514'+' /whatismytelegramid: It shows your unique Telegram ID by which the AliceBot recognises you.\n\n\t '+ u'\U0001F514'+' /help: You surely know what that is!\n\n\tThere are some easter egg commands that you must try to figure out! (hint: related to CAT)\n\n\n'
helpmsg_admin = '\t'+ u'\U0001F514'+' Administrator commands:\n\n\t '+ u'\U0001F514'+' /adddocs: To insert Documents into the folder\n\n\t '+ u'\U0001F514'+' /addreminders: To include the next reminder for the date\n\n'
helpmsg_feedback = 'Do you like this Bot? Rate this bot on the Bot Store so that more can benefit! <link>'
