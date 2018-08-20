import discord, re
client = discord.Client()


TOKEN = 'NDc1Nzk1MTYzOTE0OTYwOTA2.Dkq6Iw.Q6WEKvJQxZahi7-BTy7334-uLN4'
url = 'https://us17.campaign-archive.com/?u=b0c288d012c3990e6593e76e1&id=79473da32d&e=eb0d880e49'

resumeRegex = re.compile(r'learn\.joma\.io|joma\'?s (?:resume|cv)', re.IGNORECASE)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    resumeResult = resumeRegex.match(message.content)

    if(resumeResult):
        msg = 'Hello {0.author.mention}, here\'s the link to Joma\'s CV! {1}'.format(message, url)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Running')

client.run(TOKEN)