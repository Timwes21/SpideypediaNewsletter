from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv
load_dotenv()


api_key=os.environ["GOOGLE_API_KEY"]


llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", api_key=api_key)

