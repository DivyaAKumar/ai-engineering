#recursive charachter text splitter for markdown
from langchain_text_splitters import RecursiveCharacterTextSplitter, Language
text = '''
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

    def study(self, subject):
        print(f"{self.name} is studying {subject}.")

    def get_details(self):
        return {
            "name": self.name,
            "age": self.age
        }


class College:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def show_college(self):
        print(f"College: {self.name}")
        print(f"Location: {self.location}")


student = Student("Divya", 22)
student.introduce()
student.study("Artificial Intelligence")

college = College("Bhilai Institute of Technology", "Durg")
college.show_college()
'''
#initialize the splitter
splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size = 300,
    chunk_overlap = 0

)
#perform the split
chunks = splitter.split_text(text)
print(len(chunks))
print(chunks[1])
