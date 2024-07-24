import discord
from discord.ext import commands

# Your bot token
TOKEN = 'YOUR_BOT_TOKEN_HERE'

# Create an instance of a bot
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True  # Enable message content intent
bot = commands.Bot(command_prefix='!', intents=intents)

# Dictionary to store user preferences
user_preferences = {}

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
    print('------')
    # Set custom status
    activity = discord.Game(name="!help for commands")
    await bot.change_presence(status=discord.Status.online, activity=activity)

@bot.command(name='notify', help='Set the channel and keywords to monitor. Usage: !notify #channel-name keyword1 keyword2 ...')
async def notify(ctx, channel: discord.TextChannel, *keywords):
    user_id = ctx.message.author.id
    if user_id not in user_preferences:
        user_preferences[user_id] = {}
    user_preferences[user_id]['channel'] = channel.name
    user_preferences[user_id]['keywords'] = list(keywords)
    await ctx.send(f'You will be notified for keywords: {", ".join(keywords)} in {channel.mention}')

@bot.command(name='show', help='Show your current keyword subscriptions. Usage: !show')
async def show(ctx):
    user_id = ctx.message.author.id
    if user_id in user_preferences:
        preferences = user_preferences[user_id]
        channel = preferences.get('channel')
        keywords = preferences.get('keywords', [])
        await ctx.send(f'You are subscribed to keywords: {", ".join(keywords)} in #{channel}')
    else:
        await ctx.send('You have no keyword subscriptions.')

@bot.command(name='remove', help='Remove keywords from your subscription. Usage: !remove keyword1 keyword2 ...')
async def remove(ctx, *keywords):
    user_id = ctx.message.author.id
    if user_id in user_preferences:
        for keyword in keywords:
            if keyword in user_preferences[user_id]['keywords']:
                user_preferences[user_id]['keywords'].remove(keyword)
        await ctx.send(f'Keywords {", ".join(keywords)} have been removed from your subscription.')
    else:
        await ctx.send('You have no keyword subscriptions.')

@bot.command(name='help', help='Show a list of available commands and how to use them.')
async def help_command(ctx):
    help_text = (
        "**Available Commands:**\n"
        "- **!notify #channel-name keyword1 keyword2 ...** - Set the channel and keywords to monitor.\n"
        "- **!show** - Show your current keyword subscriptions.\n"
        "- **!remove keyword1 keyword2 ...** - Remove keywords from your subscription.\n"
        "- **!help** - Show this help message."
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
