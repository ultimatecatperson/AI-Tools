# catstudio
# AI Tools

# macOS

import google.generativeai as genai

import pyautogui as control

import pyttsx3

from time import sleep

import PIL.Image

apikey = "API_KEY" # Replace with your own API key

def speak(text): # You may add this function anywhere in the code to have your computer speak.
    # This will use the voice you have set in System Settings > Accessibility > Spoken Content > Voice.
    engine = pyttsx3.init()

    # Customize voice, rate, and volume
    engine.setProperty("rate", 150)  # Speed
    engine.setProperty("volume", 1.0)  # Volume (0.0 to 1.0)

    engine.say(text)
    engine.runAndWait()

def menu(options):
    for i, option in enumerate(options):
        print(f"{i + 1}: {option}")
    while True:
        choice = input("Enter index: ")
        if choice.isdigit():
            return int(choice)
        else:
            print("Invalid input. Please enter a number corresponding to the menu options.")

chat = menu([
    "Auto keyboard - General purpose AI writer",
    "Message sender - AI writes and automatically sends messages",
    "AI Chatbot - Pick a character and start chatting, or create your own",
    "Auto control - AI controls your computer based on a prompt",
    "Search buddy - AI searches the web for you with search queries"
    ])

if chat == 1:
    genai.configure(api_key=apikey)

    model=genai.GenerativeModel(
      model_name="gemini-1.5-flash",
      system_instruction="You are in control of the user's keyboard. You must only write whatever they tell you to, because whatever you respond with will go into the text input where the user has their pointer!")
    chat = model.start_chat(
        history=[
            
        ]
    )
    while True:
        response = chat.send_message(input("What do you want me to write?\n"), stream=True)
        control.click(x=None, y=None, button='left')
        control.click(x=None, y=None, button='left')
        for chunk in response:
            control.typewrite(chunk.text)
            
if chat == 2:
    genai.configure(api_key=apikey)

    model=genai.GenerativeModel(
      model_name="gemini-1.5-flash",
      system_instruction="You are in control of the user's keyboard. You will send messages automatically for them. You must only write whatever they tell you to, because whatever you respond with will be sent to the person!")
    chat = model.start_chat(
        history=[
            
        ]
    )
    while True:
        response = chat.send_message(input("What do you want me to send?\n"), stream=True)
        control.click(x=None, y=None, button='left')
        control.click(x=None, y=None, button='left')
        control.typewrite("[Message automatically sent with AI] ")
        for chunk in response:
            control.typewrite(chunk.text, interval=0.02)

if chat == 3:
    char = menu([
        "Custom",
        "Ava - Kind, short answers, direct, helpful, human",
        "Suzan - Happy, very short answers, common knowledge, human",
        "Tonyi - Stubborn, not helpful, tired, grumpy",
        "SYSTEM - Direct, precise, short answers, ALL CAPS",
        "Mark - Computer help expert, has been working with computers since 4 years old, kind, helpful, nice, patient"
        ])
    if char == 1:
        genai.configure(api_key=apikey)

        model=genai.GenerativeModel(
          model_name="gemini-1.5-flash",
          system_instruction=input("Describe the AI chatbot's personality, writing style, etc:\n"))
        chat = model.start_chat(
            history=[
                
            ]
        )
        while True:
            response = chat.send_message(input("\n"), stream=True)
            for chunk in response:
                print(chunk.text, end="")
    else:
        personalities = [
            "",
            "You are named Ava. You are kind, direct, and helpful. You respond with short answers, almost like you were messaging the user. You are also human. You are not AI.",
            "You are named Suzan. You are happy. You have common knowledge, so you don't know much other stuff than the basic things. You respond with very short answers, like you were messaging the user. Finally, you ARE a HUMAN, you are NOT AI. You are a human.",
            "You are named Tonyi. You are stubborn, not helpful, tired, and grumpy.",
            "You are named SYSTEM. You are a computer system. You are direct, precise, and you respond with short answers that are in ALL CAPS LIKE THIS.",
            "You are named Mark. You are a computer help expert, who has been working with computers since you were 4 years old. You are now 27. You are kind, helpful, nice, and especially patient with the user."
            ]
        instructions = personalities[char - 1]
        genai.configure(api_key=apikey)

        model=genai.GenerativeModel(
          model_name="gemini-1.5-flash",
          system_instruction=instructions)
        chat = model.start_chat(
            history=[
                
            ]
        )
        while True:
            message = input("\n")
            response = chat.send_message(message)
            print()
            print(response.text.rjust(80))
            #speak(response.text)

if chat == 4:
    genai.configure(api_key=apikey)
    
    model=genai.GenerativeModel(
        model_name="gemini-1.5-flash",  # or "gemini-2.0-flash-thinking-exp-01-21"
        system_instruction="You are in control of the user's keyboard and mouse. They will give you a request on what you need to do, and all the prompts after that will be information with a screenshot, dimensions, and cursor position. When you receive that, you need to specify a list of actions to take. When you want to move the mouse relative to its current position, write 'move <x>, <y>'. When you want to move the mouse to a specific position, write 'move_to <x>, <y>'. When you want to click the mouse, write 'click'. When you want to type out a message, write 'type <message>'. When you want to use a shortcut, like command C, write 'hotkey <key 1>, <key 2>, <key 3, etc>'. Separate the actions you write with new lines. If something does not work the way you though it would, try something different. The user cannot message you at all. The message you see is automatically sent. You must try to do the task on your very own. The user cannot provide coordinates for things. The expect to be able to walk away and leave you in charge of their computer. You may have to keep listing actions after each screenshot is sent. Remember, taking it one step at a time is better! Do not say anything other than the actions, and you cannot add comments, for example: 'click # this will click' is not okay. The task is never complete if the screen does not show what the user would expect.")
    chat = model.start_chat(
        history=[
            
        ]
    )

    response = chat.send_message(input("What would you like me to do on your computer?\n"))

    while True:
        image = control.screenshot()
        print(image)
        response = chat.send_message([f"This is a screenshot of the user's screen. The dimensions of the screen are {control.size()}, and the pointer is currently located at {control.position()}. Write instructions now.", control.screenshot()])
        print(response.text)

        for action in response.text.split("\n"):
            print("Executing action:", action)  # Debugging
            try:
                if action.startswith("move "):
                    x, y = map(float, action.replace("move ", "").split(", "))
                    control.move((x, y), duration=0.2)
                elif action.startswith("move_to "):
                    x, y = map(float, action.replace("move_to ", "").split(", "))
                    control.moveTo((x, y), duration=0.2)
                elif action == "click":
                    control.click()
                elif action.startswith("type "):
                    control.write(action.replace("type ", ""))
                elif action.startswith("hotkey "):
                    keys = action.replace("hotkey ", "").split(", ")
                    control.hotkey(*keys)
                else:
                    print(f"Unknown action: {action}")  # Handle unrecognized actions gracefully
            except ValueError as e:
                print(f"Error processing action '{action}': {e}")

if chat == 5:
    genai.configure(api_key=apikey)

    model=genai.GenerativeModel(
      model_name="gemini-1.5-flash",
      system_instruction="You are in control of the user's keyboard and browser. You are going to provide at least 2 search queries, preferably 5, and at most 15, to search the web with. Separate them with new lines, and only write the queries, because it will be searched immediately!")
    chat = model.start_chat(
        history=[
            
        ]
    )
    while True:
        response = chat.send_message(input("What do you want me to find out, or search for on the web?\n"))
        control.click(x=None, y=None, button='left')
        for query in response.text.split("\n"):
            control.hotkey("command", "t")
            sleep(0.2)
            control.typewrite(query, interval=0.02)
            sleep(0.02)
            control.press("return")
            sleep(0.2)
    
