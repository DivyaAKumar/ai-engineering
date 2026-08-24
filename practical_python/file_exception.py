from pathlib import Path

path = Path("data.txt")

try:
    with path.open("r", encoding="utf-8") as file:
        content = file.read()

except FileNotFoundError:
    print("The file does not exist.")

else:
    print(content)

finally:
    print("File operation completed.")

#pathlib 
from pathlib import Path

path = Path("data.txt")

try:
    content = path.read_text(encoding="utf-8")
    print(content)

except FileNotFoundError:
    print("File not found.")