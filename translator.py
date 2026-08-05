from pathlib import Path

class WBTextFile:
    def __init__(self, filename):
        self.filename = Path(filename)
        self.lines = []

    def load(self):
        with open(self.filename, "r", encoding="utf-8", errors="ignore") as f:
            self.lines = f.readlines()

    def save(self, filename=None):
        target = filename or self.filename

        with open(target, "w", encoding="utf-8", newline="\n") as f:
            f.writelines(self.lines)

    def stats(self):
        print(f"Файл: {self.filename.name}")
        print(f"Строк: {len(self.lines)}")
class QuickStrings(WBTextFile):

    def parse(self):

        result = []

        for number, line in enumerate(self.lines):

            line = line.rstrip()

            if not line:
                continue

            parts = line.split(" ", 1)

            if len(parts) != 2:
                continue

            ident = parts[0]
            text = parts[1]

            result.append({
                "line": number,
                "id": ident,
                "text": text
            })

        return result
      
    
if __name__ == "__main__":

    qs = QuickStrings("source/quick_strings.txt")

    qs.load()

    data = qs.parse()

    print("Найдено строк:", len(data))

    print()

    for row in data[:20]:
        print(row)
