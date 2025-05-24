![ai-tools-banner](https://github.com/user-attachments/assets/f0212da0-d4e4-42eb-a742-3d664be7b0ec)

# AI-Tools

# How to set up

## Step 0 - Setup Python (skip this if you already have Python)

Go to https://www.python.org/downloads/ to download Python onto your computer.

Once downloaded, use the Python setup window to set up Python.

## Step 1 - Download files

Click the Python file that shows your OS, then "Download".

## Step 2 - Install libraries with pip

Open Terminal (macOS, Windows) or Command line (Linux), and enter the following commands:

If you are using Windows and you did not already have Python, you will need to add the path for it to your PATH environmental variable.

```bash
pip install -q -U google-generativeai pyautogui Pillow pyttsx3
```

and if that doesn't work, try

```bash
pip3 install -q -U google-generativeai pyautogui Pillow pyttsx3
```

If that still doesn't work and you're on Windows, you need to set up your environmental variable PATH for Python.

The first command is absolutely required. This will allow you to use Google Gemini through my app. The second command is required only is you want Gemini to be able to use your keyboard and mouse. If you don't install it, then you'd have to delete the `import pyautogui as control` line in the code, and then you can only use the chatbot.

## Step 3 - Get a Gemini API key

You need a Google Account. Go to https://aistudio.google.com/app/apikey, sign in, and click "Create API Key". Copy the key.

On macOS, right click on the `ai_tools.py` file and select "Open with..." > "IDLE.app". Linux is similar.
On Windows, right click on the `ai_tools.py` file and select "Show more options" > "Edit with IDLE" > "Edit with IDLE [...]"

Remove `API_KEY` and paste your own there.

## Step 4 - Use and set up for easy access

You can now open the `ai_tools.py` file and use the tools! **If you use macOS, you will have to allow "Terminal" to access accessibility shortcuts by opening System Settings > Privacy & Security > Accessibility and toggle Terminal to on.** You can drag the file to your destop for easy access. Make sure it opens with "Python Launcher".


# How to use

Open `ai_tools.py` and select the tool you want to use by typing the number beside it and pressing `enter`.

Each tool is used a little differently. Each is explained below.

To switch tools or get out of one, you have to close and reopen the program. You can even have multiple tools running at once! (To do that, you'd need multiple Terminal/Command Prompt windows running AI Tools)

## How to select

Simply type the number beside the option you want and press `enter`.

## Auto keyboard

When you're in the tool, type out your prompt. DO NOT PRESS `enter`! Move your cursor to where you want it to type. DO NOT CLICK! Make sure the window running AI Tools is in focus and then press `enter`. The program will click and start typing. You can follow up with Gemini.

## Message sender

This works in exactly the same way as **Auto Keyboard**, but it's optimized for message sending. For example, it types "[Message automatically sent with AI]" at the beginning and it types slower. You can follow up with Gemini on messages.

## AI Chatbot

When you're in the tool, simply select the personality preset you want to chat with, or you can make your own! If you want to create your own, select 1 ("Custom"), type the personality (these are the system instructions that Gemini will follow), and press `enter`.

Once you've selected your personality, you can start chatting. Type your message and press `enter`. Gemini will respond, keeping in mind its personality it has to mimic and your recent messages.

## Auto control

Hoo hoo, this is FUN. **Before using, read the warning below.** Once you're in the tool, you can type out your prompt (tell it what to do in detail) and press `enter`. The program will take a screenshot, send that with the pointer's position and screen resolution to Gemini, and Gemini will output multiple actions that you will be able to see in the program's window. Be sure to allow Python and/or Terminal to record your screen and use accessibility shortcuts if you're on macOS. This only accepts one prompt per use.

**WARNING: THIS TOOL HAS FULL ACCESS TO YOUR KEYBOARD AND MOUSE INPUT AND IS NOT VERY ACCURATE. PLEASE DO NOT TRUST THIS FULLY AT ALL UNTIL THIS WARNING IS GONE.**
**SAFETY FEATURES INCLUDED: THIS TOOL MOVES THE MOUSE SLOWLY AND WITH DELAY SO THAT YOU CAN STILL HAVE CONTROL. THERE IS ALSO A FAILSAFE INCLUDED AUTOMATICALLY. TO USE IT, MOVE YOUR CURSOR TO A CORNER OF YOUR SCREEN WHEN THE PROGRAM IS IN CONTROL. WHEN IT IS NOT IN CONTROL, SIMPLY QUIT THE PROGRAM BY PRESSING `control` `c` (ANY OS, EVEN macOS).**

## Search buddy

Open your web browser (I use [DuckDuckGo](https://duckduckgo.com/app/devices)!!!!!!!!!!!!), and type your prompt. DO NOT PRESS `enter` YET. Move your cursor to the URL text input of your web browser window. DO NOT CLICK! Press `enter`. The tool will take Gemini's queries and open tabs and search them. You can follow up with Gemini on your searches.

## File editor

Simple. When you're in the tool, type your file's path (if it's in the same folder as AI Tools, then all you have to do is type the name, and if it's in a subfolder or multiple, simply type the folders past AI Tools), and press `enter`. The file's source text will show. Now, type your prompt (describe how you want the file changed in detail) and press `enter`. The file will magically change with Gemini's edits. If you do not see the edits with the file open, close it and reopen it because any program you're using to see it (like TextEdit or Notepad) won't show any changes until you open it after the tool has made edits. You can follow up with Gemini on it. To choose a different file, you would need to close and reopen AI Tools.
