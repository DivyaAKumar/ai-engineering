from langchain_text_splitters import RecursiveCharacterTextSplitter

text = '''My name is Divya
I am 22 years old

I live in Bhilai
How are you'''

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 10,
    chunk_overlap= 0,
)
chunks = splitter.split_text(text)
print(len(chunks))
print(chunks)

