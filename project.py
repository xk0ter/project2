import requests
import telebot

bot_token = "8988223029:AAGPvPHsqFmigvJ9kHrvLON5CY-rWKzsFQc"
weather_api_key = "6adb650537e01fcfde933851d051ac0b"

bot = telebot.TeleBot(bot_token)# экземпляр класса telebot
# обработка команды страрт для запуска бота
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "привет напиши мне название любого города мира и я пришлю текущую погоду")

@bot.message_handler(func=lambda message: True)# назначает функцию обработчиком для любых сообщений
def get_weather(message):
    city = message.text.strip()
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}&units=metric&lang=ru"
    try:
        response = requests.get(url) #отправляет гет запрос по указанному url
        data = response.json()#преобразует ответ от сервера openweathermap который приходит в формате json
        # в структуру данных python
        if data.get("cod") != 200:
            bot.reply_to(message, "город не найден проверьте название и попробуйте снова")
            return
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        description = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        itog = (f"город: {city}\n"
                  f"температура: {round(temp)}°C\n"
                  f"ощущается как: {round(feels_like)}°C\n"
                  f"погода: {description}\n"
                  f"влажность: {humidity}%\n"
                  f"ветер: {wind_speed} м/с")
        bot.reply_to(message, itog)
    except Exception as a:
        bot.reply_to(message, "произошла ошибка при получении данных попробуйте позже.")

if __name__ == "__main__":
    bot.polling(none_stop=True)





