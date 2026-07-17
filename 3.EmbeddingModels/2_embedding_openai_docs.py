from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

embedding = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001"
)

documents = [
    "Delhi is the capital of India",
    "Kolkata is the capital of West Bengal",
    "Paris is the capital of France"
]

vectors = embedding.embed_documents(documents)

print("Number of vectors:", len(vectors))
print("Dimension of one vector:", len(vectors[0]))
print(vectors[0][:10])   # First 10 values of the first vector