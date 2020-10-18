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
        result, embed = create_tag(message, message_parts)
    elif(command == "delete"):
        result, embed = delete_tag(message, message_parts)
    elif(command == "help"):
        embed = tags_commands.help()
    elif(command == " "):
        embed = tags_commands.nocommand()
    else:
        result, embed = normal_tag(command)

    return result, embed
        
def create_tag(message, message_parts):
    """
    Creates a tags
    message - the discord message object
    message_parts - the parts of the message (tag) (create) tagname tagcontents 
    """
    embed  = None
    result = None

    separator = ' '
    if(len(message_parts) < 3):
        embed = tags_commands.notenoughargs()
        return result, embed
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
        tag_collection.insert_one(mydict)
    except mongo_error.DuplicateKeyError:
        embed = tags_commands.taginuse()
    except Error as e :
        embed = tags_commands.tagerror()
        raise e

    else:
        embed = tags_commands.tagsucceed()

    return result, embed


def delete_tag(message, message_parts):
    """
    Deletes a tags
    message - the discord message object
    message_parts - the parts of the message (tag) (delete) tagname 
    """
    embed  = None
    result = None

    if(len(message_parts) < 3):
        embed = tags_commands.notenoughargs()
        return result, embed

    # get tagname
    tagname = message_parts[2]

    db = database.DBClient().get_db()
    tag_collection = db.Tags2020

    myquery = { "tag": tagname, "owner_id" : message.author.id }

    try:
        result = tag_collection.delete_one(myquery)
    except:
        embed = tags_commands.tagerror()
    else:
        if(result.deleted_count == 1):
            embed = tags_commands.tagdelete()
        else:
            embed = tags_commands.notagdelete()
    
    return result, embed

def normal_tag(command):
    embed  = None
    result = None
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