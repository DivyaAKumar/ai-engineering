from langchain_community.document_loaders import CSVLoader

loader= CSVLoader(file_path=r'D:\pythonProj\python-for-ai\RAG\DocumentLoaders\patient_insurance_data.csv')
data = loader.load()
print(data[0])