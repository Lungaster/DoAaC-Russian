from parser import WarbandParser
from writer import Writer
from validator import Validator


def translate(text: str) -> str:
    """
    Пока заглушка.
    Здесь позже будет OpenAI/Gemini/Ollama.
    """
    return text


def main():

    parser = WarbandParser("source/quick_strings.txt")

    entries = parser.parse()

    print(f"Загружено {len(entries)} строк")

    translated = 0

    for entry in entries:

        new_text = translate(entry.original)

        Validator.validate(entry.original, new_text)

        entry.translated = new_text

        translated += 1

    Writer.save(
        "translated/quick_strings.txt",
        entries
    )

    print(f"Готово. Обработано {translated} строк.")


if __name__ == "__main__":
    main()
