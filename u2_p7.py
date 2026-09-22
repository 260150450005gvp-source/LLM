from google import genai
from dotenv import load_dotenv
import os
import csv
import time


load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

result = []
total_token = 0
Successful = 0
failed = 0

with open("prompt.csv", "r", encoding="utf-8") as file:

    reader = csv.reader(file)

    for row in reader:

        prompt = row[0]

        print("\nprocessing:", prompt)

        start_time = time.time()

        try:

            response = client.models.generate_content(
                model="gemini-3.5-flash-lite",
                contents=prompt
            )

            end_time = time.time()
            response_time = end_time - start_time

            print("Total time:", response_time)

            answer = response.text

            token = len(answer.split())

            cost = token * 0.00001

            total_token += token
            Successful += 1

            print("Response:", answer)
            print("Response time:", response_time)
            print("Estimated tokens:", token)
            print("Estimated API cost:", cost)

            result.append([
                prompt,
                answer,
                "Success",
                response_time,
                token,
                cost
            ])

        except Exception as e:

            failed += 1

            print("Status: Failed")
            print("Error:", e)

            result.append([
                prompt,
                "",
                "Failed",
                0,
                0,
                0
            ])

        # Delay for rate limit
        time.sleep(2)


# Save Result

with open("results.csv", "w", encoding="utf-8", newline="") as file:

    writer = csv.writer(file)

    writer.writerow([
        "Prompt",
        "Response",
        "Status",
        "Response Time",
        "Estimated Tokens",
        "Estimated Cost"
    ])

    writer.writerows(result)


print("\nTotal Prompts:", Successful + failed)
print("Successful Requests:", Successful)
print("Failed Requests:", failed)
print("Total Estimated Tokens:", total_token)
print("Total Estimated Cost:", total_token * 0.000001)