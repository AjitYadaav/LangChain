# from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

# model = ChatOpenAI(model='gpt-4')
model = ChatGoogleGenerativeAI(
    model='gemini-2.5-flash',
    temperature = 0
    # max_completion_tokens = 10
)

result = model.invoke("Suggest me 5 best Motivational movies.")
print(result.content)