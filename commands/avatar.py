import discord

async def main(self, message):
    user = message.author

    mention = message.mentions[0] if len(message.mentions) > 0 else False

    content = message.content.split()
    given_content_list = content[2:]
    given_content = " ".join(given_content_list)

    nickname_mention = False
    for i in message.guild.members:
        # Looking for the exact nickname match (non-case sensitive)
        if (str(given_content).lower() == str(i.display_name).lower()):
            nickname_mention = i

    return_string = ""
    if(mention):
        return_string = mention.avatar_url
    elif(nickname_mention):
        return_string = nickname_mention.avatar_url
    else: 
        return_string = user.avatar_url
    
    await message.channel.send(return_string)