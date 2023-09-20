import os
import openai
import fun
import json

#openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key ="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"


f=open('data/history.txt', 'r',encoding='utf-8')
history = f.read()

# print(history )

m=open('data/meal.txt', 'r', encoding='utf-8')
meal = m.read()

schedule=fun.school_schedule()

# print(schedule )
# exit()

with open('data/jedol.json', 'r',encoding='utf-8') as f:
    systemData = json.load(f)


messages =systemData
messages.append({"role": "system", "content": f"{history}"} )
messages.append({"role": "system", "content": f"{schedule}"} )
messages.append({"role": "system", "content": f"{meal}"} )


while True:
    user_input = input("me  \t: ")
    if  user_input =="": break
    messages.append({"role": "user", "content": user_input})

    aiObj = openai.ChatCompletion.create(
       model="gpt-4",

        messages= messages
    )
    
    
    response=aiObj['choices'][0]['message']['content']
    print(f"제돌\t: {response}")
    # messages.append({"role": "assistant","content": response})