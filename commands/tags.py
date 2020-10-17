from models import database, tags_commands
import datetime
from bson.objectid import ObjectId
from bson.timestamp import Timestamp
import pymongo.errors as mongo_error

async def main(self, message):
    
    # removing hashtag, could probably combine these two lines
    tag_command = message.content.split(' ', 1)[1]

    message_parts = tag_command.split(' ')
    command = message_parts[1] if len(message_parts) > 1 else " "

    result, embed = handle_tag_commands(command, message, message_parts)

    # returning embed if error or help
    if not embed:   
        await message.channel.send(result)
    else:
        await message.channel.send(embed=embed)  

        
def handle_tag_commands(command, message, message_parts):
    """
    Handles the different types of tag commands
    command - the specific command if any the user wants for the tag
    message - the user's message object for populating specific tag details in db
    """
    embed  = None
    result = None

    # TODO make delete and list functions
    if(command == "create"):

        separator = ' '
        # create tagname tagcontent
        tagname = message_parts[2]

        # (create), (tagname), (content)
        # remove the create and tagname from message
        del message_parts[:3]
        tag_contents = separator.join(message_parts)

        # create mongo object
        oid = ObjectId()
        mydict = {
        "_id": oid, 
        "tag": tagname,
        "server_id":message.channel.id,
        "owner_id":message.author.id,
        "content": tag_contents,
        "timestamp":Timestamp(datetime.datetime.today(), 0)}

        # Get our db instance
        db = database.DBClient().get_db()
        tag_collection = db.Tags2020

        # error handling
        try:
            x = tag_collection.insert_one(mydict)
        except mongo_error.DuplicateKeyError:
            embed = tags_commands.taginuse()
        except:
            embed = tags_commands.tagerror()
        else:
            embed = tags_commands.tagsucceed()

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
        

