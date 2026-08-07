from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

response = client.responses.create(
    model="gpt-5.5",
    input="Ответь одним предложением: кто ты?"
)

print(response.output_text)