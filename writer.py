from pathlib import Path

from parser import TranslationEntry


class Writer:

    @staticmethod
    def save(filename: str, entries: list[TranslationEntry]):

        path = Path(filename)

        path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with open(
            path,
            "w",
            encoding="utf-8",
            newline="\n"
        ) as file:

            for entry in entries:

                text = (
                    entry.translated
                    if entry.translated
                    else entry.original
                )

                file.write(
                    f"{entry.identifier} {text}\n"
                )
