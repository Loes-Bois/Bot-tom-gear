import random

async def main(self, message):
    # All the possible story strings that can be given
    all_action_strings = [
        "disembowels a critically endangered gorrila",
        "derails the polar express using five pounds of sugar and a flame thrower",
        "starts WWIII",
        "eats a Big Mac medium meal and dies",
        "commits arson",
        "weaponizes a Toyota pickup truck",
        "single handedly wipes Kansas off the map",
        "renovates a garden for charity",
        "takes an old lady out for dinner",
        "fulfills a terminally ill child's dream of driving in a pink lamborghini"
    ]
    # The amount of people to select
    num_people = 3
    # Get three random strings
    random_strings = random.sample(all_action_strings, num_people)
    # Random users that will be used in the message
    random_users = random.sample(message.guild.members, num_people)
    # The string that is returned at the end
    story_str = ""
    
    # Create the story
    for i in range(len(random_users)):
        user = random_users[i]
        string = random_strings[i]

        if (i == len(random_users) - 1):
            story_str += f"and <@{user.id}> {string}"
        else:
            story_str += f"<@{user.id}> {string},"
            story_str += "\n"

    await message.channel.send(story_str)