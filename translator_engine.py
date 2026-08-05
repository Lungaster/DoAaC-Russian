from __future__ import annotations

import json
from pathlib import Path


class TranslatorEngine:

    def __init__(self, glossary_path="glossary.json"):

        self.glossary = {}

        path = Path(glossary_path)

        if path.exists():
            self.glossary = json.loads(
                path.read_text(
                    encoding="utf-8"
                )
            )

    def apply_glossary(self, text: str):

        for original, translated in self.glossary.items():

            text = text.replace(
                original,
                translated
            )

        return text

    def translate(self, text: str):

        text = self.apply_glossary(text)

        return text
