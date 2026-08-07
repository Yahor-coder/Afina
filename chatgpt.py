from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)


def ask_gpt(question):

    response = client.responses.create(
        model="gpt-5.5",
        input=question
    )

    return response.output_text