import telebot
import time
import datetime as DT
import random
from telebot import types # для указание типов

bot = telebot.TeleBot('6489274618:AAEgR7soWskyw-vUPqFs_8neo6MGYrxu_uw');

CHAT_BY_DATETIME = dict()

random_orel_reshka = random.choices(['Орел', 'Решка'])

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    btn2 = types.KeyboardButton("🕹️ Мини-игры")
    btn3 = types.KeyboardButton("🪙")
    markup.add(btn1, btn2, btn3)
    
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я тестовый бот @e_looney".format(message.from_user), reply_markup=markup)
    
@bot.message_handler(content_types=['text'])
def func(message):

    if(message.text == "👋 Поздороваться"):
        bot.send_message(message.chat.id, text="Привеет..")
        bot.send_message(message.chat.id, text="👋")
        time.sleep(5)
        
        
    elif(message.text == "🕹️ Мини-игры"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🎲 Кубик")
        btn2 = types.KeyboardButton("🎰 Слоты")
        btn3 = types.KeyboardButton("🎳 Боулинг")
        btn4 = types.KeyboardButton("⚽ Футбол")
        btn5 = types.KeyboardButton("🏀 Баскетбол")
        btn6 = types.KeyboardButton("🎯 Дартс")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn3)
        markup.add(btn4, btn5, btn6)
        markup.add(back)
        bot.send_message(message.chat.id, text="Выбирите игру", reply_markup=markup)

    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("👋 Поздороваться")
        button2 = types.KeyboardButton("🕹️ Мини-игры")
        button3 = types.KeyboardButton("🪙")
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    
    elif(message.text == "🎲 Кубик"):
        value = bot.send_dice(message.chat.id, emoji='🎲').dice.value # указываем боту отправлять анимацию кубика (можно заменить смайлик на другой который указан в списке в начале телеграфа) и сразу записывать результат в переменную 'value'
        time.sleep(.5) # программа ждет 0.5 секунд
        bot.send_message(message.chat.id, 'Вам выпало...') # бот отправляет сообщение 
        time.sleep(5) # программа ждет 5 секунд
        bot.send_message(message.chat.id, f'Число {value}!') # бот отправляет результат
        
    elif(message.text == "🎰 Слоты"): 
        value = bot.send_dice(message.chat.id, emoji='🎰').dice.value
        time.sleep(.5) # программа ждет 0.5 секунд
        bot.send_message(message.chat.id, 'Вам выпало...') # бот отправляет сообщение 
        time.sleep(5) # программа ждет 5 секунд
        bot.send_message(message.chat.id, f'Число {value}!') # бот отправляет результат
        
    elif(message.text == "🎳 Боулинг"): 
        value = bot.send_dice(message.chat.id, emoji='🎳').dice.value
        time.sleep(.5) # программа ждет 0.5 секунд
        bot.send_message(message.chat.id, 'Вам выпало...') # бот отправляет сообщение 
        time.sleep(5) # программа ждет 5 секунд
        bot.send_message(message.chat.id, f'Число {value}!') # бот отправляет результат
        
    elif(message.text == "⚽ Футбол"): 
        value = bot.send_dice(message.chat.id, emoji='⚽').dice.value
        time.sleep(.5) # программа ждет 0.5 секунд
        bot.send_message(message.chat.id, 'Вам выпало...') # бот отправляет сообщение 
        time.sleep(5) # программа ждет 5 секунд
        bot.send_message(message.chat.id, f'Число {value}!') # бот отправляет результат
        
    elif(message.text == "🏀 Баскетбол"): 
        value = bot.send_dice(message.chat.id, emoji='🏀').dice.value
        time.sleep(.5) # программа ждет 0.5 секунд
        bot.send_message(message.chat.id, 'Вам выпало...') # бот отправляет сообщение 
        time.sleep(5) # программа ждет 5 секунд
        bot.send_message(message.chat.id, f'Число {value}!') # бот отправляет результат
        
    elif(message.text == "🎯 Дартс"): 
        value = bot.send_dice(message.chat.id, emoji='🎯').dice.value
        time.sleep(.5) # программа ждет 0.5 секунд
        bot.send_message(message.chat.id, 'Вам выпало...') # бот отправляет сообщение 
        time.sleep(5) # программа ждет 5 секунд
        bot.send_message(message.chat.id, f'Число {value}!') # бот отправляет результат
        
    #Пользователь ввел "Орел" или "Решка" - значит это игра
    if message.text == "🪙":
        flip = random.randint(0, 1)
        if flip == 0:
            bot.send_message(message.chat.id,'Ты угадал\n')
        else:
            bot.send_message(message.chat.id,'Не угадал\n')
    
    
        
        
        
        
bot.polling(none_stop=True)
