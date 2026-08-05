import re

VAR_PATTERN = re.compile(r"\{[^}]+\}")

SPECIAL_SYMBOLS = [
    "^",
    "@",
    "|",
    "<",
    ">",
    "%",
]


class ValidationError(Exception):
    pass


class Validator:

    @staticmethod
    def variables(text: str):

        return sorted(VAR_PATTERN.findall(text))

    @staticmethod
    def special(text: str):

        result = []

        for symbol in SPECIAL_SYMBOLS:

            result.extend([symbol] * text.count(symbol))

        return sorted(result)

    @classmethod
    def validate(cls, original: str, translated: str):

        original_vars = cls.variables(original)
        translated_vars = cls.variables(translated)

        if original_vars != translated_vars:

            raise ValidationError(
                f"""
Переменные не совпадают

Оригинал:
{original_vars}

Перевод:
{translated_vars}
"""
            )

        original_special = cls.special(original)
        translated_special = cls.special(translated)

        if original_special != translated_special:

            raise ValidationError(
                f"""
Спецсимволы повреждены

Оригинал:
{original_special}

Перевод:
{translated_special}
"""
            )

        return True
