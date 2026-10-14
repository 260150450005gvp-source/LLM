
import json
import os

from dotenv import load_dotenv

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser, StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.chat_history import InMemoryChatMessageHistory
from pydantic import BaseModel, Field
from typing import List
from langchain_core.messages import get_buffer_string


load_dotenv()
class EmailEvaluation(BaseModel):
    evaluation: dict = Field(description="Email evaluation")
    identified_issues: List[str] = Field(description="Problems found")
    suggestions: List[str] = Field(description="Suggestions for improvement")
    improved_email: str = Field(description="Improved email")
# 1. Initialize chat history
chat_history = InMemoryChatMessageHistory()

api = os.getenv("GEMINI_API_KEY")


# 2. Take input from user
email_purpose = input("Enter your email purpose: ")
email_type = input("Enter recipient type (HOD, Manager, Client):")
email_information = input("Enter information: ")
email_ton = input("Enter your Email tone: ")


# 3. Save user information in history
chat_history.add_user_message(
    f"""
Purpose: {email_purpose}
Type: {email_type}
Information: {email_information}
Tone: {email_ton}
"""
)


# 4. Format chat history
formatted_buffer = get_buffer_string(chat_history.messages)


# STAGE 1 - EMAIL GENERATOR


prompt_template = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are an email writing assistant. "
        "Write clear, professional and concise emails."
    ),

    (
        "human",
        """
Write an email for:

Email Purpose: {email_purpose}
Recipient Type: {email_type}
Email Information: {email_information}
Email Tone: {email_ton}
"""
    )
])


# 5. Initialize Gemini model
chat_model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",
    api_key=api
)


# 6. Output parser
output_parser = StrOutputParser()
email_parser = PydanticOutputParser(
    pydantic_object=EmailEvaluation
)
# 7. First chain
first_chain = prompt_template | chat_model | output_parser


# 8. Generate email
generated_email = first_chain.invoke({
    "email_purpose": email_purpose,
    "email_type": email_type,
    "email_information": email_information,
    "email_ton": email_ton
})



# STAGE 2 - EMAIL CHECKER




checker_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
Check the email for:
- Grammar
- Clarity
- Tone
- Professionalism
- Completeness
- Subject line

Return the evaluation, identified issues, suggestions, and improved email.

{format_instructions}
"""
    ),
    (
        "human",
        """
Check this email:
{generated_email}
"""
    )
])


# 9. Second chain
second_chain = checker_prompt | chat_model | email_parser


# 10. Check generated email
checked_email = second_chain.invoke({
    "generated_email": generated_email,
    "format_instructions": email_parser.get_format_instructions()
})



# OUTPUT PARSER

try:
 email_result = checked_email.model_dump()
except Exception:
    email_result = {
        "evaluation": {},
        "identified_issues": [],
        "suggestions": [],
        "improved_email": checked_email
    }



# DISPLAY GENERATED EMAIL

print("\n" + "=" * 60)
print(" GENERATED EMAIL")
print("=" * 60)

print("\nSubject:")
print(generated_email.splitlines()[0].replace("Subject:", "").strip())

print("\nEmail Body:")
print("\n".join(generated_email.splitlines()[1:]).strip())



# DISPLAY EMAIL EVALUATION

print("\n" + "=" * 60)
print(" EMAIL EVALUATION")
print("=" * 60)

evaluation = email_result.get("evaluation", {})

print("Grammar:", evaluation.get("grammar", ""))
print("Clarity:", evaluation.get("clarity", ""))
print("Tone:", evaluation.get("tone", ""))
print("Professionalism:", evaluation.get("professionalism", ""))
print("Completeness:", evaluation.get("completeness", ""))
print("Subject Line:", evaluation.get("subject_line", ""))


# DISPLAY IDENTIFIED ISSUES


print("\n" + "=" * 60)
print(" IDENTIFIED ISSUES")
print("=" * 60)

for issue in email_result.get("identified_issues", []):
    print("-", issue)



# DISPLAY SUGGESTIONS


print("\n" + "=" * 60)
print(" SUGGESTIONS")
print("=" * 60)

for suggestion in email_result.get("suggestions", []):
    print("-", suggestion)



# DISPLAY IMPROVED EMAIL

print("\n" + "=" * 60)
print(" IMPROVED EMAIL")
print("=" * 60)

print(email_result.get("improved_email", ""))



# DISPLAY CHAT HISTORY

print("\n" + "=" * 60)
print(" CHAT HISTORY")
print("=" * 60)

print("Total messages:", len(chat_history.messages))
