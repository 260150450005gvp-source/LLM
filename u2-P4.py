import time
from google import genai


api_key=(input("enter api key:"))
model_name=(input("enter model name:"))
Temperature=float(input("enter phront tempreture:"))
Top_p=float(input("top_p:"))
Maximum_Tokens=int(input("maximum tokken"))

if Temperature>=0 and Temperature<=1:
    temp=Temperature
else:
    print("enter value of temperature between 0 and 1")

if Top_p>=0 and Top_p <=1:
    top__p=Top_p
else:
    print("enterr value of top_p between 0 and 1")



response_list=[]

client = genai.Client(api_key=api_key)
while True:
    user_prompt = input("Enter Text:")
    if user_prompt.lower()=="exit":
        print("nice to meet you, goodbyee")
        break
    else:
        response_list.append({"role":"user","content":user_prompt})
        start=time()
        interaction = client.interactions.create(
        model=model_name,
        input=user_prompt,
        generation_config={
            "Top_p":Top_p,
            "Maximum_Tokens":Maximum_Tokens,
            "Temperature":Temperature
        }
    )

    response_all=interaction.output_text
    print(response_all)
    end=time()
    print(interaction.model)
    print(end-start)
    response_list.append({"role":"Assistsnt","content":response_all})


