# import the necessary packages
import numpy as np
import io
import discord
import math

from models import image_load, image_warp as warp, read_messages as readm


async def main(self, message):

    message_parts = message.content.split(" ")

    url = message.attachments[0].url if len(message.attachments) > 0 else False

    # if no attachment check for embeddeds
    url = message.embeds[0].url if len(message.embeds) > 0 else url

    url = message_parts[2] if (len(message_parts)) > 2 else url

    #TODO read recent message on channel to find latest image and make it scuffed
    # await readm.find_recent_image(message.channel.id, message.id)
    
    if(url):
        data = await image_load.url_to_image(url, message)

        magic_image_data = make_magic(data)

        bits = image_load.bts_to_img(magic_image_data)

        f = io.BytesIO(bits)
        attachment = discord.File(f , 'cool_image.png')

        await message.channel.send(file=attachment)
    else:
        await message.channel.send("I would like an image please :D")


def make_magic(image):
    
    warped = warp.wrap_image(image)

    return warped

