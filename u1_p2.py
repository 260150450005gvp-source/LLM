data= {
        "GPT_4":
        {
            "Developer":"OpenAI ",
            "Open_Source/Proprietary":"Proprietary ",
            "Multimodal_Support(Yes/no)":"Yes ",
            "typical_Use_Cases":"1.Code Review,2.Content Generation 3.Document Summarization"
        },

          "Claude_3":
        {
            "Developer":"Anthropic",
            "Open_Source/Proprietary":"Proprietary ",
            "Multimodal_Support(Yes/no)":"Yes",
            "typical_Use_Cases":"1.Content Generation, 2..Code Review 3.Code Generation "
        },

          "Gemini":
        {
            "Developer":"Gemini ",
            "Open_Source/Proprietary":"Proprietary",
            "Multimodal_Support(Yes/no)":"Yes ",
            "typical_Use_Cases":"1.Function Calling,2.Legal & Financial Analysis "
        },

          "Llama_3":
        {
            "Developer":"Llama_3 ",
            "Open_Source/Proprietary":"Open-Source",
            "Multimodal_Support(Yes/no)":"No ",
            "typical_Use_Cases":"1.AI Chatbots & Virtual Assistants,2.Code Generation & Developm,3.Content Generation "
        },

          "Mistral":
        {
            "Developer":"Mistral ",
            "Open_Source/Proprietary":"Both (Open-Source & Proprietary) ",
            "Multimodal_Support(Yes/no)":"Yes ",
            "typical_Use_Cases":"1.Code Generation & Development, ,2.AI Chatbots & Customer Support "
}
}

print("Please select option")
print("GPT_4")
print("Claude_3")
print("Gemini")
print("Llama_3")
print("Mistral")

choice=str(input("Enter Your choice "))
print(choice)

if choice=="GPT_4":
  print(data['GPT_4'])
elif choice=="Claude_3":
  print(data['Claude_3'])
elif choice=="Gemini":
  print(data['Gemini'])
elif choice=="Llama_3":
  print(data['Llama_3'])
elif choice=="Mistral":
  print(data['Mistral'])
else:
  print("enter currect name")
