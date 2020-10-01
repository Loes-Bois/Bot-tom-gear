from urllib.request import urlopen
import cv2
import io
import aiohttp


#TODO make use of OAuth to read recent messages so we can call this endpoint
async def find_recent_image(channel_id, message_id):

    url = f"https://cdn.discordapp.com/channels/{channel_id}/messages/{message_id}?before=true&limit=20"
    messages = None
    print(messages)
    print(url)  
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status != 200:
                messages = None
            messages = io.BytesIO(await resp.read())

    