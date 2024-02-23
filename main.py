import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    # Place API Key Here
    api_key=os.environ.get("OPENAI_API_KEY"),
)


messages = []

system_msg = "Hi I have a test next week. I am going to paste my notes and I need you to convert them into a format that is easy for me to make index cards. I need you to separate them with a pipe |. Pretend you are making quizlet or anki cards so that I can pass my test! I need them in the format of 'front of index card' | 'back of index card' | 'question category'. The front of the index card should be a question. The back of the index card should be the answer. And the category should be specific so I can group them. For an example, if the note said Apples can come in many different colors but most of the time apples are red. You could make the front of the card: What colors are apples usually, then make the back of the card |Red typically, but they can range in many different colors, and category would be: Colors of Fruits. The output would then be What colors are apples usually | Red typically but they can range in many different colors | Colors of Fruits"
messages.append({"role": "system", "content": system_msg})

print("Please enter the name of your file")
print("Note, it will be in the format of <filename>-anki-bot-deck.txt")
file_name = input()

notes = ""

print("Please enter your notes!")
while True:
    notes = input()
    
    if(notes=="exit"):
        break

    messages.append({"role": "user", "content": notes})
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages)
    reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    f = open(f"{file_name}-anki-bot-deck.txt", "a")
    f.write("\n"+reply+"\n")
    f.close()
    print("Notes successfully added!")
    print("\n"+'Are there any more notes? Type "exit" to exit the session'+"\n")