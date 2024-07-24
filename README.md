# DiscordNotifier
While initially made for the ADSBx Discord, I wanted to put the code out here for everyone. I'm a complete novice at this and ChatGPT did help with some of the code, so be weary of that. It runs fine for me on Python 3 and Windows. 

# How to Set Up, Customize, and Deploy Your Discord Notification Bot

This guide will walk you through setting up Python, creating and customizing your Discord notification bot, and deploying it on your server. The bot allows users to set up notifications for specific keywords in specific channels and provides commands for managing these notifications.

## Step 1: Setting Up Python

1. **Download Python**:
   - Visit the [Python website](https://www.python.org/downloads/) and download the latest version of Python.
   - Make sure to check the option to add Python to your PATH during installation.
   - Don't know how to add to PATH? Follow these steps:
      1. Right-click My Computer (either on the Desktop or the Start menu). Click Properties.
      2. In the System Properties dialog box, click the Advanced tab.
      3. Click Environment Variables.
      4. In the top list, scroll down to the PATH variable, select it, and click Edit. 
          - Note: If the PATH variable does not exist, click New and enter PATH for the Variable Name.
      5. In the Variable Value box, scroll to the end of the variable. 
          - If there is no semi-colon (;) at the end of the current path, add one, and then enter the path to the MicroStation folder.
      6. Click OK to close each dialog box.

2. **Verify Installation**:
   - Open a command prompt or terminal.
   - Type the following command to verify that Python is installed correctly:
     ```bash
     python --version
     ```
   - You should see a version number printed out, confirming the installation.

3. **Install `discord.py`**:
   - In the command prompt or terminal, install the `discord.py` library using pip:
     ```bash
     pip install discord.py
     ```
     Note: You may need to use `pip3` instead of `pip`, depending on your version of Python. 

## Step 2: Creating a Discord Bot Account

1. **Go to the Discord Developer Portal**:
   - Navigate to the [Discord Developer Portal](https://discord.com/developers/applications).

2. **Create a New Application**:
   - Click on "New Application".
   - Give your application a name and click "Create".

3. **Create a Bot**:
   - In your application, go to the "Bot" section.
   - Click "Add Bot" and confirm by clicking "Yes, do it!".

4. **Get Your Bot Token**:
   - Under the "Bot" section, click "Copy" under the "TOKEN" section. Keep this token safe and never share it.

5. **Enable Privileged Gateway Intents**:
   - Under "Privileged Gateway Intents", enable "MESSAGE CONTENT INTENT".

## Step 3: Inviting Your Bot to Your Server

**Important Note before inviting the bot to your server:**

In the same folder as `bot.py`, create a file named user_preferences.json (if you didn't clone the repo). This will ensure user settings are retained. No personal data is stored, here's an example of the output when a user wants to be notified: 

[DiscordNotifier/image.png]

There's a blank user_preferences.json file in this repo. 

1. **Generate an OAuth2 URL**:
   - Go to the "OAuth2" section.
   - Under "OAuth2 URL Generator", select the `bot` scope.
   - In the "Bot Permissions" section, select the necessary permissions:
     - `Read Messages/View Channels`
     - `Send Messages`
     - `Manage Messages`
     - `Read Message History`

2. **Invite the Bot**:
   - Copy the generated URL.
   - Paste the URL into your browser and select the server where you want to add the bot.
   - Authorize the bot to join your server.

## Step 4: Customizing the Bot Script

1. **Download the bot.py file in this repo**
2. **Fire up your favorite code/text editor. I prefer Notepad++**
3. **Customize the Bot Token**:
   - Replace `'YOUR_BOT_TOKEN_HERE'` with the bot token you copied from the Discord Developer Portal.

4. **Customize Command Prefix and Names (Optional)**:
   - If you prefer different command names or a different prefix, update the `command_prefix` and the command names in the script. For example, change the `command_prefix` from `'!'` to `'/custom-'` or any other prefix you prefer.
  
## Troubleshooting

- **Bot Not Responding**: Ensure the bot is running in the command prompt or terminal.
- **Permissions Issues**: Verify that the bot has the necessary permissions in the server.
- **Message Content Not Detected**: Ensure the "MESSAGE CONTENT INTENT" is enabled in the Discord Developer Portal.
