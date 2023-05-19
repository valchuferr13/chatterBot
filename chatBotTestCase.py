import unittest
import threading
import requests


class TestChatbot(unittest.TestCase):
    def test_saludo(self):
        response = requests.post(
            'http://127.0.0.1:5000/chatbot',
            json={'message': 'Hola'}
        )

        self.assertEqual(
            response.json()['response'],
            'Hola! En qué puedo ayudarte?'
        )

    def test_respuesta_predeterminada(self):
        response = requests.post(
            'http://127.0.0.1:5000/chatbot',
            json={'message': 'Esto es un mensaje no reconocido'}
        )
        self.assertEqual(response.json()['response'],
                         'Lo siento, no entendí eso.'
                         )

    def test_multiples_solicitudes(self):
        # Definir la función para enviar una solicitud al chatbot
        def send_request(message):
            response = requests.post(
                'http://127.0.0.1:5000/chatbot',
                json={'message': message}
            )
            return response.json()

        messages = ['Hola', 'Hola!', 'Buenos días', 'Cómo estás?']

        # Crear una lista para almacenar las respuestas
        responses = []

        # Crear hilos para enviar las solicitudes simultáneamente
        threads = [
            threading.Thread(
                target=lambda r=responses, m=msg: r.append(send_request(m))
            ) for msg in messages
        ]

        # Iniciar los hilos
        for thread in threads:
            thread.start()

        # Esperar a que todos los hilos finalicen
        for thread in threads:
            thread.join()

        # Verificar las respuestas
        expected_responses = [
            'Hola! En qué puedo ayudarte?',
            'Hola! En qué puedo ayudarte?',
            'Lo siento, no entendí eso.',
            'Lo siento, no entendí eso.'
        ]

        for message, response, expected_response in zip(
                messages, responses, expected_responses):
            print(f"Message: {message}")
            print(f"Expected: {expected_response}")
            print(f"Actual: {response['response']}")
            self.assertEqual(response['response'],
                             expected_response)


if __name__ == '__main__':
    unittest.main()
