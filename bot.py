import discord
import os_helper

# Load env variables
from dotenv import load_dotenv
load_dotenv()

import commands.handle_cmd as cmds

class BottomBot(discord.Client):
    # Set the token to pound on default
    bot_keyword = "#"

    async def on_ready(self):
        print(f"Logged in as {self.user}!")

    async def on_message(self, message):
        # Dont respond on ourselves
        if message.author == self.user:
            return

        if message.content.startswith(self.bot_keyword):
            await cmds.handle(self, message)

        if message.content == "ping":
            await message.channel.send("pong")

try:
    # Get the token
    bot_token = os_helper.get_env_var("BOT_TOKEN")

    if (bot_token is None):
        raise Exception("A token was not passed as a environment variable")

    # Start the bot
    client = BottomBot()
    client.run(bot_token)
except Exception as err:
    # Catch and print any errors
    print(f"FATAL: {err}")
