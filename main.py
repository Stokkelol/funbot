from telegram import Bot
from dotenv import load_dotenv, find_dotenv
import requests
import os
from datetime import datetime
from datetime import date

load_dotenv(find_dotenv())

owm_endpoint = "https://api.openweathermap.org/data/2.5/forecast?q=kiev&appid="
owm_token = os.getenv("OPENWEATHERMAP_API_KEY")
abs_min = 273.15
token = os.getenv('TELEGRAM_API_KEY')

telegram_endpoint = 'https://api.telegram.org/bot'
chat_id = os.getenv('CHAT_ID')

first_date = date(2020, 3, 16)

class FunBot:
    api = Bot(token)

    def greet(self) -> str:
        today = date.today()
        diff = (first_date - today).days

        return f"Morning! It's {diff} day of quarantine! Wish you a pleasant day!"

    def prepare(self, response):
        res = []
        for item in response['list']:
            res.append(self.prepare_item(item))

        return res

    @staticmethod
    def get_forecast():
        res = requests.get(owm_endpoint + owm_token)

        if res.status_code != 200:
            return "error getting response"

        return res.json()

    @staticmethod
    def prepare_item(item):
        return item

    @staticmethod
    def get_updates():
        res = requests.get(telegram_endpoint + token + '/getUpdates')

        return res.content

    @staticmethod
    def temp_to_celsius(temp):
        return temp - abs_min

    @staticmethod
    def prepare_time(timestamp):
        return datetime.fromtimestamp(timestamp)


def main():
        bot = FunBot()
        message = bot.greet()
        bot.api.send_message(chat_id, message)


if __name__ == '__main__':
    main()
