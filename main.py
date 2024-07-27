import telebot
from Token_Scarab import Scrab_tokenbaz
from configure import API_KEY
import time

bot = telebot.TeleBot(API_KEY)

channel_id = "@tether_pulse"
admin_id = 836821716 

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Welcome to token baz bot")
    for i in Scrab_tokenbaz():
        bot.send_message(message.chat.id, f"""<b>{i['Name_and_type']}</b> 
🔵قیمت <b>خرید</b> تتر از شما : <b><code>{i["Buy_price"]}</code></b>
🔴قیمت <b>فروش</b> تتر به شما : <b><code>{i["Sell_price"]}</code></b>
کارمزد تراکنش : <b>{i["Wage"]} </b>
""", parse_mode="HTML")

@bot.message_handler(commands=['adminscrabing'])
def send_to_channel(message):
    if message.from_user.id != admin_id:
        bot.send_message(message.chat.id, "You are not authorized to use this command.")
        return

    while True:
        try:
            for i in Scrab_tokenbaz():
                bot.send_message(channel_id, f"""<b>{i['Name_and_type']}</b> 
    🔵قیمت <b>خرید</b> تتر از شما : <b><code>{i["Buy_price"]}</code></b>
    🔴قیمت <b>فروش</b> تتر به شما : <b><code>{i["Sell_price"]}</code></b>
    کارمزد تراکنش : <b>{i["Wage"]} </b>
    """, parse_mode="HTML")
        except Exception as e:
            print(f"An error occurred: {e}")
            time.sleep(2)
        bot.send_message(channel_id, "💯-- @tether_pulse --💯")
        time.sleep(60)

bot.infinity_polling()