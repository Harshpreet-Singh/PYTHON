# from openai import OpenAI

# client = OpenAI(
#     api_key = "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",
# )

# completion = client.chat.completion.create(
#     model="gpt-4.1",
#     messages=[
#         {"role": "system", "content": "You are a virtual assistant Jarvis, skilled in general tasks like alexa and google"},
#         {"role": "user", "content": "What is coding"}
#     ]
#     # input="Write a one-sentence bedtime story about a unicorn."
# )

# print(completion.choices[0].messages.content)
import openai

client = openai.OpenAI(api_key="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")

response = client.completions.create(
    model="gpt-3.5-turbo",
    prompt="Write a one-sentence bedtime story about a unicorn."
)

print(response.choices[0].text)
