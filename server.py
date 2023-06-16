from flask import Flask
import random

app = Flask(__name__)

random_number = random.randint(0,10)

@app.route('/')
def hello():
    return "<div><h1>Guess a number between 0 and 9</h1><img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/></div>"

@app.route('/<number>')
def response(number):
    int_number = int(number)
    aux_text = ''
    if int_number > random_number:
        aux_text = "<div><h1>It is lower ;(</h1><img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/></div>"
    elif int_number < random_number:
        aux_text = "<div><h1>It is higher ;(</h1><img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/></div>"
    else:
        aux_text = "<div><h1>CORRECT!</h1><img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/></div>"

    return aux_text

if __name__ == "__main__":
    app.run(debug=True)