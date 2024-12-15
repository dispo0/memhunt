from flask import Flask, request, jsonify
import telebot
import os

# Заменить на свой токен
API_TOKEN = '8120908173:AAE29D0SP5MaYxuOglT1QeUs0c74aYcRnFY'
bot = telebot.TeleBot(API_TOKEN)

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "MemMaster API работает!"})

@app.route('/webhook', methods=['POST'])
def webhook():
    json_str = request.get_data().decode('UTF-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return '', 200

# Запуск сервера
if __name__ == '__main__':
    app.run(debug=True)