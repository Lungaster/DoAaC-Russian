from parser import WarbandParser
from writer import Writer
from validator import Validator
from translator_engine import TranslatorEngine
from progress import Progress


def main():

    engine = TranslatorEngine()

    progress = Progress()

    parser = WarbandParser(
        "source/quick_strings.txt"
    )

    entries = parser.parse()

    total = len(entries)

    print(f"Найдено {total} строк")

    translated = 0

    for entry in entries:

        result = engine.translate(
            entry.original
        )

        Validator.validate(
            entry.original,
            result
        )

        entry.translated = result

        translated += 1

    Writer.save(
        "translated/quick_strings.txt",
        entries
    )

    progress.data["translated"] = translated

    progress.save()

    print(
        f"Переведено {translated}/{total}"
    )


if __name__ == "__main__":
    main()
