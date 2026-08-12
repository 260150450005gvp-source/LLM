from dotenv import load_dotenv
import os
load_dotenv()
os.getenv("GEMINI_API_KEY")
import time

from google import genai

client = genai.Client()


user_prompt = input("Enter Text:")

start=time.time()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=user_prompt
)

end=time.time()

total_time=end-start

characters=len(user_prompt)
word=len(user_prompt.split())



print(interaction.output_text)
print(f"characters lenth:{characters}")
print(f"word lenth:{word}")
print(f"Total Processing Time:{total_time}")
print("Model Name:",interaction.model)



if word<50:
    print("Short")
elif word<=150:
    print("Medium")
else:
    print("Long")

print(interaction)