from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters, CallbackContext
import requests

# OpenWeatherMap API key
OWM_API_KEY = open('OWM_key.txt').read().strip()  # if you want to store it more securely: as an environment variable
# Telegram bot token
TOKEN = open('token.txt').read().strip()

OPENWEATHER_API_URL_CITIES = 'http://api.openweathermap.org/data/2.5/group'
OPENWEATHER_API_URL_WEATHER = 'http://api.openweathermap.org/data/2.5/weather'


def start(update: Update, context: CallbackContext):
    first_name = update.effective_chat.first_name
    message = f"Hola {first_name}! Soy un bot de previsión del tiempo. Puedes seleccionar una ciudad de la lista o escribir el nombre de una ciudad."

    # Create inline keyboard with city options
    cities = get_predefined_cities()
    buttons = [[InlineKeyboardButton(city["name"], callback_data = f"weather_{city['id']}")] for city in cities]
    reply_markup = InlineKeyboardMarkup(buttons)

    context.bot.send_message(chat_id=update.effective_chat.id, text=message, reply_markup=reply_markup)


def get_predefined_cities():
    api_url = OPENWEATHER_API_URL_CITIES
    params = {
        'id': '3128760,3105600,3117735,3105184,5128581',  # IDs of cities BCN, Vilafranca, Madrid, Vilanova, New York
        'units': 'metric',
        'appid': OWM_API_KEY,
    }
    response = requests.get(api_url, params=params)
    data = response.json()
    return data.get("list", [])


def handle_text(update: Update, context: CallbackContext):
    text = update.message.text.lower()

    predefined_cities = get_predefined_cities()

    if text in predefined_cities:
        city_id = next(city['id'] for city in predefined_cities if city['name'].lower() == text)
        weather(update, context, city_id)
    else:
        fetch_weather_directly(update, context, text)


def fetch_weather_directly(update: Update, context: CallbackContext, city_name: str):
    api_url = OPENWEATHER_API_URL_WEATHER
    params = {'q': city_name, 'units': 'metric', 'appid': OWM_API_KEY }

    response = requests.get(api_url, params=params)
    data = response.json()

    if 'name' in data:
        send_weather_info(update, context, data)
    else:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=f"City not found. Please select a city from the list or try again.")


def send_weather_info(update: Update, context: CallbackContext, data: dict):
    weather_description = data['weather'][0]['description']
    temperature = data['main']['temp']
    feels_like = data['main']['feels_like']
    temp_min = data['main']['temp_min']
    temp_max = data['main']['temp_max']
    humidity = data['main']['humidity']
    icon_code = data['weather'][0]['icon']

    # Map icon code to OpenWeatherMap icon URL
    icon_url = f"https://openweathermap.org/img/wn/{icon_code}@2x.png"

    message = (
        f"Weather in {data['name']}:\n\n"
        f"Description: {weather_description}\n"
        f"Temperature: <b>{temperature}°C</b>\n"
        f"Feels like: {feels_like}°C\n"
        f"min: {temp_min}°C  Max: {temp_max}°C\n\n"
        f"Humidity: {humidity}%"
    )

    # Send message with weather information and include the weather icons
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=icon_url, caption=message, parse_mode=ParseMode.HTML)


def weather(update: Update, context: CallbackContext, city_id: int):
    api_url = OPENWEATHER_API_URL_WEATHER
    params = {
        'id': city_id,
        'units': 'metric',
        'appid': OWM_API_KEY,
    }

    response = requests.get(api_url, params=params)
    data = response.json()

    if response.status_code == 200:
        send_weather_info(update, context, data)
    else:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text = f"Unable to fetch weather information for the selected city.")


def main():
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CallbackQueryHandler(button_callback))  # Add CallbackQueryHandler without a pattern
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_text))

    updater.start_polling()
    updater.idle()


def button_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    city_id = int(query.data.split('_')[1])
    weather(update, context, city_id)

# To ensure that the main() function is called only when the script is executed directly, not when imported as a module
if __name__ == '__main__':
    main()
