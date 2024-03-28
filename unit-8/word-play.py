from pathlib import Path

ROOT_DIR = Path(__file__).parent
TEXT_FILE = ROOT_DIR / 'words.txt'
# Modern way
contents = TEXT_FILE.read_text()
# print(contents)
fin = open(TEXT_FILE)
print(fin)

for line in fin:
    word = line.strip()
    print(line)