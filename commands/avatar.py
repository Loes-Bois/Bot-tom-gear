import discord

async def main(self, message):
    user = message.author

    mention = message.mentions[0] if len(message.mentions) > 0 else False

    return_string = ""
    if(mention):
        return_string = mention.avatar_url
    else: 
        return_string = user.avatar_url
    
    await message.channel.send(return_string)