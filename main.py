#Импорт
from flask import Flask, render_template,request, redirect
import os


app = Flask(__name__)
#Запуск страницы с контентом
@app.route('/')
def index():
    return render_template('index.html')


#Динамичные скиллы
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    email = request.form.get('email')
    text = request.form.get('text')
    message = "Соопщ отправлено"
    filee = "TEXT.txt"
    print(message)
    with open(filee, 'w') as file:
        file.write(text)
        file.write(email)
    return render_template('index.html', button_python=button_python, message=message)

if __name__ == "__main__":
    app.run(debug=True)
