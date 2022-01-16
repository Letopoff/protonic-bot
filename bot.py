import telebot
import configure
import random
import time
import requests

from telebot import types
from configure import open_weather_token

weather = telebot.TeleBot(configure.config['token'])
bot = telebot.TeleBot(configure.config['token'])

@bot.message_handler(commands = ['start'])
def start(message):
    info_client = types.KeyboardButton('Информация о боте')
    function_client = types.KeyboardButton('Функции')
    things = types.KeyboardButton('Полезные функции')
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    markup.add(function_client, info_client, things)
    bot.send_message(message.chat.id, 'Привет, {0.first_name} !'.format(message.from_user), reply_markup = markup)
    time.sleep(0.2)
    bot.send_message(message.chat.id, 'Меня зовут Протоник! Будем знакомы\n\nМоя задача стать твоим путеводителем по миру IT')

@weather.message_handler(content_types='text')
def get_weather(message):
    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric"
        )
        data = r.json()
        gorod = data['name']
        cur_weather = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind_speed = data['wind']['speed']
        print(gorod)
        bot.send_message(message.chat.id, str(f'Погода в городе: {gorod}\nТемпература : {cur_weather}C°\nВлажность: {humidity}%\nДавление {pressure} мм.рт.ст\nВетер: {wind_speed} м/с'))
    except Exception as ex:
        bot.send_message(message.chat.id, (ex))
        bot.send_message(message.chat.id, 'Проверьте название города')

@bot.message_handler(content_types='text')
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'Информация о боте':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            function_bot = types.KeyboardButton('Что умеет данный бот?')
            technology_bot = types.KeyboardButton('На каких технологиях создан бот')
            version_bot = types.KeyboardButton('Версия')
            back = types.KeyboardButton('🔙Назад')
            markup.add(function_bot, technology_bot, version_bot, back)
            bot.send_message(message.chat.id, 'Для интересующей вас информации нажмите кнопки на клавиатуре', reply_markup = markup)
        
        elif message.text == 'Погода':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            back = types.KeyboardButton('🔙Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Введите ваш город')
            bot.register_next_step_handler(message, get_weather)

        elif message.text == 'Число от 1 до 100':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            back = types.KeyboardButton('🔙Назад')
            markup.add(back)
            bot.send_message(message.chat.id, random.randint(0,100), reply_markup = markup)

        elif message.text == 'Полезные функции':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            random_button = types.KeyboardButton('Число от 1 до 100')
            weather_button = types.KeyboardButton('Погода')
            back = types.KeyboardButton('🔙Назад')
            markup.add(random_button, weather_button, back)
            bot.send_message(message.chat.id, 'Выберите интересующую вас функцию', reply_markup = markup)

        elif message.text == 'Что умеет данный бот?':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            back = types.KeyboardButton('🔙Назад')
            markup.add(back)
            time.sleep(0.2)
            bot.send_message(message.chat.id, 'Привет!\nДанный бот был создан с целью помочь людям познакомиться с чудесным миром IT\n\nФункционал бота позволяет узнать краткое описание интерусующего вас направления')

        elif message.text == 'На каких технологиях создан бот':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            back = types.KeyboardButton('🔙Назад')
            markup.add(back)
            time.sleep(0.2)
            bot.send_message(message.chat.id, 'Этот бот создан на основе библиотеки telebot (pyTelegramBotAPI) для языка Python')

        elif message.text == 'Версия':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            back = types.KeyboardButton('🔙Назад')
            markup.add(back)
            time.sleep(0.2)
            bot.send_message(message.chat.id, 'Версия бота 1.2.0\n\nВерсия Python - 3.10.1 64 bit')

        elif message.text == 'Функции':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('Профориентация')
            types_it = types.KeyboardButton('Направления IT')
            back = types.KeyboardButton('🔙Назад')
            markup.add(item1,types_it, back )
            bot.send_message(message.chat.id, 'Умения бота', reply_markup = markup)

        elif message.text == 'Профориентация':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            back = types.KeyboardButton('🔙Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Узнайте, подоходит ли вам IT сфера\n(Но вообще такие тесты не работают, решать кем вы станете можете только вы сами @daMpleto)\n\n https://vuzopedia.ru/podbor-professii', reply_markup = markup)

        elif message.text == 'Дизайн':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            back = types.KeyboardButton('🔙Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Дизайн - Красивый выбор)')
            time.sleep(0.2)
            bot.send_message(message.chat.id, 'Все чаще сегодня на слуху появляются такие термины, как IT-дизайн проекта или IT-архитектура предприятия, все чаще становится востребованной услуга IT-архитектора. Давайте вместе разбираться, из какой оперы этот персонаж и кому он может быть полезен.\nНачнем с аналогии: когда у нас появляется идея построить дом мы в первую очередь идем на сайт архитекторного бюро и выбираем проект, который подходит по внешнему виду и соответствует нашим ожиданиям по планировке и функционалу помещений.\nТак и в мире информационных технологий — прежде, чем внедрять какие-либо сервисы или решения, вводить в эксплуатацию новые сервера либо запускать схемы их бесперебойной и отказоустойчивой работы, необходимо четко прорисовать полную схему их внедрения и конечного использования на предприятии. Если внедрять что-либо без правильного подхода и без планирования инфраструктуры, может оказаться, что решение либо не соответствует задачам бизнеса, либо не сможет использоваться полноценно.')
            time.sleep(0.2)
            bot.send_message(message.chat.id, 'Сборник курсов по it дизайну - https://tilda.education/articles-online-web-design-courses')

        elif message.text == 'Направления IT':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            design = types.KeyboardButton('Дизайн')
            itsecurity = types.KeyboardButton('Информационная безопасность')
            web_prog = types.KeyboardButton('Веб-разработка')
            app_create = types.KeyboardButton('Создание приложений')
            start_prog= types.KeyboardButton('"Просто попробовать"')
            back = types.KeyboardButton('🔙Назад')
            markup.add(itsecurity, web_prog, design, app_create, start_prog, back)
            bot.send_message(message.chat.id, 'Выберите интересующий вас раздел', reply_markup = markup)

        elif message.text == 'Создание приложений':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            back = types.KeyboardButton('🔙Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Сборник курсов', reply_markup = markup)
            time.sleep(0.2)
            bot.send_message(message.chat.id, 'https://vc.ru/flood/29258-podborka-kursov-po-sozdaniyu-mobilnyh-prilozheniy', reply_markup = markup)

        elif message.text == '"Просто попробовать"':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            back = types.KeyboardButton('🔙Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Начните с простого - Python', reply_markup = markup)
            time.sleep(0.2)
            bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=XKHEtdqhLK8&ab_channel=BroCode', reply_markup = markup)

        elif message.text == 'Веб-разработка':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            back = types.KeyboardButton('🔙Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Веб-разработка — процесс создания веб-сайта или веб-приложения. Основными этапами процесса являются веб-дизайн, вёрстка страниц, программирование на стороне клиента и сервера, а также конфигурирование веб-сервера.', reply_markup = markup)
            time.sleep(0.2)
            bot.send_message(message.chat.id, 'На основе данных видеороликов можно научиться делать сайты - \nhttps://www.youtube.com/channel/UCCXF68Da_ndcmvv_9OG75Cw/playlists?view=50&sort=dd&shelf_id=3 \nhttps://www.youtube.com/watch?v=1X8FNuy32ZM&ab_channel=webDev', reply_markup = markup)

        elif message.text == 'Информационная безопасность':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            back = types.KeyboardButton('🔙Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Мой самый любимый раздел)', reply_markup = markup)
            bot.send_message(message.chat.id, 'Информационная безопасность – это сохранение и защита информации, а также ее важнейших элементов, в том числе системы и оборудование, предназначенные для использования, сбережения и передачи этой информации.\n Другими словами, это набор технологий, стандартов и методов управления, которые необходимы для защиты информационной безопасности', reply_markup = markup)
            time.sleep(0.5)
            bot.send_message(message.chat.id, 'Дорожная карта', reply_markup = markup)
            time.sleep(0.5)
            bot.send_photo(message.chat.id, 'https://tproger.ru/s3/uploads/2021/01/1-660x880.jpeg', reply_markup = markup)
            time.sleep(0.5)
            bot.send_message(message.chat.id, 'Начало пути - https://tryhackme.com/\n\nСборник курсов по IT безопасности - https://tutortop.ru/courses_selection/kursy_po_informacionnoj_bezopasnosti/', reply_markup = markup)

        elif message.text == 'Разработчик бота':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            back = types.KeyboardButton('🔙Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Данный бот разработан Даниилом Петраченковым\n\n Github - https://github.com/Letopoff\n Telegram - https://t.me/daMpleto', reply_markup = markup)
        
        elif message.text == '🔙Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            info_robot = types.KeyboardButton('Информация о боте')
            function_robot = types.KeyboardButton('Функции')
            things = types.KeyboardButton('Полезные функции')
            markup.add(info_robot, function_robot, things)
            bot.send_message(message.chat.id, 'Выберите интерусующий вас раздел', reply_markup = markup)


bot.polling(none_stop=True)
