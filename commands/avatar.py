async def main(self, message):
    user = message.author
    return_string = user.avatar_url
    await message.channel.send(return_string)