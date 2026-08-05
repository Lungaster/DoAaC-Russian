from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import List, Iterable


@dataclass
class TranslationEntry:
    line_number: int
    identifier: str
    original: str
    translated: str | None = None


class WarbandParser:

    def __init__(self, filename: str | Path):
        self.filename = Path(filename)

    def parse(self) -> List[TranslationEntry]:

        result: List[TranslationEntry] = []

        with open(
            self.filename,
            "r",
            encoding="utf-8",
            errors="ignore"
        ) as file:

            for line_number, line in enumerate(file):

                line = line.rstrip("\n")

                if not line:
                    continue

                identifier, text = self._split(line)

                if identifier is None:
                    continue

                result.append(
                    TranslationEntry(
                        line_number=line_number,
                        identifier=identifier,
                        original=text
                    )
                )

        return result

    @staticmethod
    def _split(line: str):

        if " " not in line:
            return None, None

        left, right = line.split(" ", 1)

        return left, right

    @staticmethod
    def rebuild(
        entries: Iterable[TranslationEntry]
    ) -> list[str]:

        result = []

        for entry in entries:

            text = entry.translated

            if text is None:
                text = entry.original

            result.append(
                f"{entry.identifier} {text}"
            )

        return result
