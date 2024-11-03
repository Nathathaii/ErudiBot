import discord

client = discord.Client()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    # Prevent the bot from responding to itself
    if message.author == client.user:
        return

    # Respond to a specific command
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

# Run the bot with your token
client.run('YOUR_BOT_TOKEN_HERE')