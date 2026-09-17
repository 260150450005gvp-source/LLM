from google import genai
from dotenv import load_dotenv
import os
import time

load_dotenv()

# API
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Message
message = []

while True:

    print("\n1. Normal Response")
    print("2. Streaming Response")
    print("3. Exit")

    # User Input
    choice = input("Choose option: ")

    if choice == "3":
        print("Bye")
        break

    # Prompt
    user_input = input("Enter Prompt: ")

    message.append({
        "role": "user",
        "content": user_input
    })

    # Normal Response
    if choice == "1":

        print("Normal Response:")

        start_time = time.time()

        try:
            interaction = client.interactions.create(
                    system_instruction=user_input,
                    model="gemini-3.5-flash-lite",
                    input=user_input
            )

            answer=interaction.output_text

            print("AI Response:")
            print(answer)

            message.append({
                "role": "assistant",
                "content": answer
            })

            end_time = time.time()

            total_time = end_time-start_time

            print("Total Response Time:", total_time)

        except Exception as e:
            print("Error:", e)

    # Streaming Response
    # Streaming Response
    elif choice == "2":

     print("Streaming Response:")

    start_time = time.time()

    answer = ""
    chunk_count = 0
    first_token = True

    try:

        stream = client.interactions.create(
            model="gemini-3.5-flash-lite",
            input=user_input,
            stream=True,
        )

        print("AI Response:")

        for event in stream:

            if event.event_type == "step.delta":

                if event.delta.type == "text":

                    content = event.delta.text

                    if content:

                        chunk_count += 1

                        if first_token:
                            first_token_time = time.time() - start_time

                            print(
                                "\nTime to First Token:",
                                first_token_time,
                                "seconds"
                            )

                            first_token = False

                        print(content, end="", flush=True)

                        answer += content

        end_time = time.time()

        message.append({
            "role": "assistant",
            "content": answer
        })

        total_time = end_time - start_time

        print("\n")
        print("Total Response Time:", total_time)
        print("Number of Chunks:", chunk_count)

    except Exception as e:
        print("Streaming Error:", e)
else:
 print("Invalid Choice")