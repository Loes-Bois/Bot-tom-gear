from models import database, tags_commands

async def main(self, message):
    
    # removing hashtag, could probably combine these two lines
    tag_command = message.content.split(' ', 1)[1]

    command = tag_command.split(' ', 1)[1] if len(tag_command.split(' ')) > 1 else " "

    result, embed = handle_tag_commands(command, message)

    # returning embed if error or help
    if not embed:   
        await message.channel.send(result)
    else:
        await message.channel.send(embed=embed)  
        
    


def handle_tag_commands(command, message):
    """
    Handles the different types of tag commands
    command - the specific command if any the user wants for the tag
    message - the user's message object for populating specific tag details in db
    """
    embed  = None
    result = None

    if(command == "create"):
        # do create tings
        print("do create")
    elif(command == "help"):
        embed = tags_commands.help()
    elif(command == " "):
        embed = tags_commands.nocommand()
    else:
        # Get our db instance
        db = database.DBClient().get_db()
        tag_collection = db.Tags2020

        # search for tag
        content = tag_collection.find_one({"tag": command})

        # if we have a result return the tag contents else show error
        if(content):
            result = content['content']
        else:
            embed = tags_commands.notagfound()
    return result, embed
        

