import discord
from discord.ext import commands
import json
import os

# Your bot token
TOKEN = 'YOUR_BOT_TOKEN_HERE'

# Create an instance of a bot
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True  # Enable message content intent
bot = commands.Bot(command_prefix='!', intents=intents)

# Dictionary to store user preferences
user_preferences = {}

# Load user preferences from a JSON file
def load_preferences():
    global user_preferences
    if os.path.exists('user_preferences.json'):
        with open('user_preferences.json', 'r') as f:
            user_preferences = json.load(f)

# Save user preferences to a JSON file
def save_preferences():
    with open('user_preferences.json', 'w') as f:
        json.dump(user_preferences, f, indent=4)

@bot.event
async def on_ready():
    load_preferences()
    print(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
    print('------')
    # Set custom status
    activity = discord.Game(name="!adsbx-help for commands")
    await bot.change_presence(status=discord.Status.online, activity=activity)

@bot.command(name='adsbx-notify', help='Set the channel and keywords to monitor. Usage: !adsbx-notify #channel-name keyword1 keyword2 ...')
async def notify(ctx, channel: discord.TextChannel, *keywords):
    user_id = ctx.message.author.id
    if user_id not in user_preferences:
        user_preferences[user_id] = {}
    user_preferences[user_id]['channel'] = channel.name
    user_preferences[user_id]['keywords'] = list(keywords)
    save_preferences()
    await ctx.send(f'You will be notified for keywords: {", ".join(keywords)} in {channel.mention}')

@bot.command(name='adsbx-show', help='Show your current keyword subscriptions. Usage: !adsbx-show')
async def show(ctx):
    user_id = ctx.message.author.id
    if user_id in user_preferences:
        preferences = user_preferences[user_id]
        channel = preferences.get('channel')
        keywords = preferences.get('keywords', [])
        await ctx.send(f'You are subscribed to keywords: {", ".join(keywords)} in #{channel}')
    else:
        await ctx.send('You have no keyword subscriptions.')

@bot.command(name='adsbx-remove', help='Remove keywords from your subscription. Usage: !adsbx-remove keyword1 keyword2 ...')
async def remove(ctx, *keywords):
    user_id = ctx.message.author.id
    if user_id in user_preferences:
        for keyword in keywords:
            if keyword in user_preferences[user_id]['keywords']:
                user_preferences[user_id]['keywords'].remove(keyword)
        save_preferences()
        await ctx.send(f'Keywords {", ".join(keywords)} have been removed from your subscription.')
    else:
        await ctx.send('You have no keyword subscriptions.')

@bot.command(name='adsbx-help', help='Show a list of available commands and how to use them.')
async def help_command(ctx):
    help_text = (
        "**Available Commands:**\n"
        "- **!adsbx-notify #channel-name keyword1 keyword2 ...** - Set the channel and keywords to monitor.\n"
        "- **!adsbx-show** - Show your current keyword subscriptions.\n"
        "- **!adsbx-remove keyword1 keyword2 ...** - Remove keywords from your subscription.\n"
        "- **!adsbx-help** - Show this help message."
    )
    await ctx.send(help_text)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    for user_id, preferences in user_preferences.items():
        if 'channel' in preferences and message.channel.name == preferences['channel']:
            for keyword in preferences.get('keywords', []):
                if keyword.lower() in message.content.lower():
                    await notify_user(message, keyword, user_id)
                    break

    await bot.process_commands(message)

async def notify_user(message, keyword, user_id):
    user = await bot.fetch_user(user_id)
    message_link = f"https://discord.com/channels/{message.guild.id}/{message.channel.id}/{message.id}"
    await user.send(f'Keyword "{keyword}" mentioned in #{message.channel.name} by {message.author}: {message.content}\nLink: {message_link}')

# Run the bot
bot.run(TOKEN)
