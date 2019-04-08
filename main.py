from telegram import Bot
from dotenv import load_dotenv, find_dotenv
import requests
import os

load_dotenv(find_dotenv())

owm_endpoint = "https://api.openweathermap.org/data/2.5/weather?q=kiev&appid="
owm_token = os.getenv("OPENWEATHERMAP_API_KEY")
abs_min = 273.15
token = os.getenv('TELEGRAM_API_KEY')

telegram_endpoint = 'https://api.telegram.org/bot'
chat_id = os.getenv('CHAT_ID')


def main():
    bot = Bot(token)
    weather = prepare(get_forecast())
    bot.send_message(chat_id, weather)


def get_forecast():
    res = requests.get(owm_endpoint + owm_token)

    if res.status_code != 200:
        return "error getting response"

    return res.json()


def prepare(response):
    return response['weather']


def get_updates():
    res = requests.get(telegram_endpoint + token + '/getUpdates')

    return res.json()


def temp_to_celsius(temp):
    return temp - abs_min
