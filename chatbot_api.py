from flask import Flask, request
# import unittest

app = Flask(__name__)


@app.route('/chatbot', methods=['POST'])
def chatbot():
    data = request.get_json()
    message = data['message'].lower()

    if 'hola' in message:
        response = 'Hola! En qué puedo ayudarte?'
    elif 'chau' in message:
        response = 'Hasta luego!'
    else:
        response = 'Lo siento, no entendí eso.'

    return {'response': response}


if __name__ == '__main__':
    app.run()

