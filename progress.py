from pathlib import Path
import json


class Progress:

    def __init__(self):

        self.filename = Path("progress.json")

        if self.filename.exists():

            self.data = json.loads(
                self.filename.read_text(
                    encoding="utf-8"
                )
            )

        else:

            self.data = {
                "translated": 0,
                "files": {}
            }

    def save(self):

        self.filename.write_text(
            json.dumps(
                self.data,
                indent=4,
                ensure_ascii=False
            ),
            encoding="utf-8"
        )
