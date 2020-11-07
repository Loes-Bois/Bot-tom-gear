# import the necessary packages
from wand.image import Image
import numpy as np
import requests
import discord
import math
import wand
import io

from models import read_messages

async def main(self, message):
    message_parts = message.content.split(" ")

    # read recent messages and find image
    url = await read_messages.find_recent_image(message.channel.id, message.id)

    # read message attachments
    url = message.attachments[0].url if len(message.attachments) > 0 else url

    # if no attachment check for embeddeds
    url = message.embeds[0].url if len(message.embeds) > 0 else url
    url = message_parts[2] if (len(message_parts)) > 2 else url
    try:
        if(url):
            # Load the image from the URL
            img = load_image(url)
            img = make_magic(img, 2)

            # Convert the imge to a byte stream and place it as an attachment
            f = io.BytesIO(img.make_blob())
            attachment = discord.File(f, 'cool_image.png')

            # Send the resultant image
            await message.channel.send(file=attachment)
        else:
            await message.channel.send("Oy mate I need a image")
    except:
        print("Error loading image")
        await message.channel.send("Oy mate, there was an error making the image")


def load_image(url):
    res = requests.get(url) # Load the URL into the request library
    img = Image(file=io.BytesIO(res.content)) # Load the IMG with wand 
    return img

def make_magic(img, scale):
    # Take the image and resize it 
    img.transform(resize='800x800>')
    
    # Liquid rescale the image (the source of the "magik")
    img.liquid_rescale(width=int(img.width * 0.5), height=int(img.height * 0.5), delta_x=int(0.5 * scale) if scale else 1, rigidity=0)
    img.liquid_rescale(width=int(img.width * 1.5), height=int(img.height * 1.5), delta_x=int(1.5 * scale) if scale else 2, rigidity=0)

    return img