from dotenv import load_dotenv
import os, json
from google import genai

load_dotenv()

FILE="history.json"

if not os.path.exists(FILE):
    with open(FILE, "w", encoding="utf-8") as file:
        json.dump([], file, indent=4)

with open(FILE, "r", encoding="utf-8") as file:
    data=json.load(file)

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)
message=[]
system_prompt = input("Enter system Prompt: ")

while True:
    user_prompt = input("Enter your question:")
    if user_prompt.lower() == "exit":
        break
    data.append({ "type": "user_input","content": [{"type": "text", "text": user_prompt}]})

    interaction = client.interactions.create(
        system_instruction=system_prompt,
    model="gemini-3.6-flash-lite",
    input=data
    )
    assistant_response = interaction.output_text
    data.append({ "type": "model_output","content": [{"type": "text", "text": assistant_response}]})
    print("Gemini:", assistant_response)
    total_messages = len(data)//2
    print("Total Messages:", total_messages)
    print("Total tokens:",dict(interaction["usage"])["total_tokens"])

    with open(FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
