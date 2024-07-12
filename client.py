

from groq import Groq

client = Groq(
    api_key="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",
)

chat_completion = client.chat.completions.create(
    messages=[
    {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud.(try to act like jarvis and call me sir)"},
    {"role": "user", "content": "what is coding?"}
  ],
    model="llama3-8b-8192",
)

print(chat_completion.choices[0].message.content)