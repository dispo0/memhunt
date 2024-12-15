from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json  # получаем данные JSON
    print(data)  # можно для отладки, чтобы увидеть, что пришло
    return "OK", 200

if __name__ == '__main__':
    app.run(debug=True)
