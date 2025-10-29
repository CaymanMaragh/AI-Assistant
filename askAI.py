import os
from openai import OpenAI
from dotenv import load_dotenv




def ask_gpt(input):
    load_dotenv()
    my_api_key = os.getenv("OPEN_AI_SECRET_KEY")
    client = OpenAI(api_key=my_api_key)
    user_input = input

    response = client.chat.completions.create(
        model="gpt-5-nano",
        messages=[
            {"role": "system", "content": "You are a helpful computer assistant similar to Jarvis in Iron Man, you can answer questions with concise answers (1 sentence unless more is necessary) Do not ask a question at the end of your answer unless deemed necessary"},
            {"role": "user", "content": user_input}
        ]
    )

    return response.choices[0].message.content