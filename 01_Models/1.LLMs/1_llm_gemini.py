# from langchain_openai import OpenAI
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

# llm = OpenAI(model = "gpt-3.5-turbo-instruct")
llm = GoogleGenerativeAI(
    model="gemini-2.5-flash"
)

result = llm.invoke("Suggest me 5 best inspirational movies.")

print(result)