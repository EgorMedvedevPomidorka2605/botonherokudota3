import telebot
token = '5282023700:AAGEGCD1HtTGIyxMnoXIY8B31afoTHwudXM'
bot = telebot.TeleBot("5282023700:AAGEGCD1HtTGIyxMnoXIY8B31afoTHwudXM")
@bot.message_handler(commands=["start"])
def start(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='Хабр', url='https://habr.com/ru'))
    markup.add( telebot.types.InlineKeyboardButton(text='Стаковерфлоу', url='https://ru.stackoverflow.com/'))
    bot.send_message(message.chat.id,"Ссылка на IT-страницы ",reply_markup=markup)
@bot.message_handler(content_types=['voice'])
def onetwothree(message):
     if message.content_type == 'voice':
      bot.send_message(message.chat.id, "Моя твоя не понимать")
@bot.message_handler(commands=["Hi"])
def hi(message):
    bot.send_message(message.from_user.id, "Как тебя зовут?");
    bot.register_next_step_handler(message, get_name)
def get_name(message):
    global name;
    name = message.text;
    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?');
    bot.register_next_step_handler(message, get_surname);
def get_surname(message):
    global surname;
    surname = message.text;
    bot.send_message(message.from_user.id,'Сколько тебе лет(целое число)?');
    bot.register_next_step_handler(message, get_age);
def get_age(message):
    global age;
    age = message.text;
    bot.send_message(message.from_user.id, 'Тебе ' + age + ' лет, тебя зовут ' + name + " " + surname)
bot.polling()


