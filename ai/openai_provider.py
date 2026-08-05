from openai import OpenAI
import os

SYSTEM_PROMPT = """
Ты профессиональный локализатор Mount & Blade Warband.

Правила:

1. НЕ изменяй:
{s1}
{s2}
{reg0}
{reg1}
^
@
%
идентификаторы

2. Переводи естественным литературным русским.

3. Используй терминологию Warband.

4. Не добавляй комментариев.

5. Возвращай только перевод.
"""


class OpenAITranslator:

    def __init__(self):

        self.client = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY")
        )

    def translate(self, text):

        response = self.client.chat.completions.create(

            model="gpt-5",

            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": text
                }
            ]

        )

        return response.choices[0].message.content.strip()
