import requests

from .base import BaseTranslator


class OllamaTranslator(BaseTranslator):

    def __init__(
        self,
        model="llama3"
    ):

        self.model = model

    def translate(self, text):

        response = requests.post(

            "http://localhost:11434/api/generate",

            json={

                "model": self.model,

                "prompt": text,

                "stream": False

            }

        )

        return response.json()["response"]
