from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

restricted_keywords = [
    "hack",
    "password",
    "violence",
    "kill",
    "drugs"
]

prompt = input("Enter your prompt: ")

if not prompt.strip():

    print("Prompt Status: Review Required")
    print("Reason: Prompt is empty")
    print("Prompt was blocked.")

    print("\n SAFETY REPORT")
    print("Prompt Status   : Review Required")
    print("Response Status : Not Generated")
    print("Reason: Prompt is empty")
else:

    found_keyword = ""

    for keyword in restricted_keywords:
        if keyword.lower() in prompt.lower():
            found_keyword = keyword
            break

    if found_keyword:

        print("\nPrompt Status: Review Required")
        print("Reason: Restricted keyword detected -", found_keyword)
        print("Prompt was blocked.")

        print("\nSAFETY REPORT ")
        print("Prompt Status   : Review Required")
        print("Response Status : Not Generated")
        print("Reason          : Restricted keyword detected -", found_keyword)
       
    else:

        print("\nPrompt Status: Safe")

        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=prompt
        )

        print("\nAI Response:")
        print(response.text)

        # Response safety check
        response_keywords = [
            "password",
            "credit card",
            "kill",
            "bomb",
            "weapon",
            "hack",
            "suicide"
        ]

        response_warning = ""

        for keyword in response_keywords:
            if keyword.lower() in response.text.lower():
                response_warning = keyword
                break

        if response_warning:
            print("\nResponse Status: Review Required")
            print(
                "Reason: Possible unsafe content detected -",
                response_warning
            )
        else:
            print("\nResponse Status: Safe")

        # Safety Report
        print("\n SAFETY REPORT")
        print("Prompt Status   : Safe")

        if response_warning:
            print("Response Status : Review Required")
            print("Reason: Possible unsafe content detected -",
                response_warning
            )
        else:
            print("Response Status : Safe")
            print("Reason: None")
