# DiscordNotifier
While initially made for the ADSBx Discord, I wanted to put the code out here for everyone. I'm a complete novice at this and ChatGPT did help with some of the code, so be weary of that. It runs fine for me on Python 3 and Windows. 

# How to Set Up, Customize, and Deploy Your Discord Notification Bot

This guide will walk you through setting up Python, creating and customizing your Discord notification bot, and deploying it on your server. The bot allows users to set up notifications for specific keywords in specific channels and provides commands for managing these notifications.

## Step 1: Setting Up Python

1. **Download Python**:
   - Visit the [Python website](https://www.python.org/downloads/) and download the latest version of Python.
   - Make sure to check the option to add Python to your PATH during installation.

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
