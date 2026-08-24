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