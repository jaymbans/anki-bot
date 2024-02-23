import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    # Place API Key Here
    api_key=os.environ.get("OPENAI_API_KEY"),
)


messages = []
system_msg = '''You are an assistant who is helping automate a manual process. Users are going to send you notes and then you do a 4 step process. #1 Convert the notes to a format that would be readable on a memorization based index card service like Anki or Quizlet. (i.e. Term - Definition and/or Question - Answer) Make sure to include some extra context. For an example, if I explain the colors of fruits, you can respond with terms like "Color of an Apple| Red" rather than just saying Apple|Red, Grape|Purple #2 Make the separator between the first and second part a pipe "|" #3 write each note/term, escaping the line items with a return, like "\n" #5 add a third column to the notes with a category. For instance Apple|Red|Colors of fruit, or even Hot Sauce| Spicy | Taste of sauces #4 write it back out to the user'''
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