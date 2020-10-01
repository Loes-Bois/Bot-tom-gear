from commands import btm_gear, avatar, magic

async def handle(self, message):
    # Takes in a discord.py message
    message_content = message.content[len(self.bot_keyword) + 1:].lower()

    # Run command files here
    if (message_content == "tonight on bottom gear"):
        await btm_gear.main(self, message)
    elif (message_content.startswith("avatar")):
        await avatar.main(self, message)
    elif(message_content.startswith("magic")):
        await magic.main(self, message)
    else:
        await message.channel.send("Errrrny nice")