from models import database, tags_commands

async def main(self, message):

    db = database.DBClient().get_db()
    client = database.DBClient().get_client()
    tag_collection = db.Tags2020

    print(tag_collection)
    result = tag_collection.find_one({"tag": "First Tag"})

    print(result)
    content = result['content']


    await message.channel.send(embed=tags_commands.HELP())


def handle_tag_commands(message):
    print()

