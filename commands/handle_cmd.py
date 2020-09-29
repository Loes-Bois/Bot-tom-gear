import commands.btm_gear as btm_gear

async def handle(self, message):
    # Takes in a discord.py message
    message_content = message.content[len(self.bot_keyword) + 1:].lower()

    # Run command files here
    if (message_content == "tonight on bottom gear"):
        await btm_gear.main(self, message)
    else:
        await message.channel.send("Errrrny nice")
        