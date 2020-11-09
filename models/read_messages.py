from urllib.request import urlopen	
import cv2	
import io	
import aiohttp
import re

from dotenv import load_dotenv
load_dotenv()

import os_helper


async def find_recent_image(channel_id, message_id):	

    urlRegexImage = "^(?:http(s)?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:\/?#[\]@!\$&'\(\)\*\+,;=.]+(?:png|jpg|jpeg|svg|webp)?(.)$"

    url = f"https://discord.com/api/channels/{channel_id}/messages?before={message_id}&limit=40"
    messages = None

    bot_token = os_helper.get_env_var("BOT_TOKEN")

    headers = {'Authorization': "Bot " + bot_token} 
    async with aiohttp.ClientSession(headers=headers) as session:	
        async with session.get(url) as resp:
            if resp.status != 200:	
                messages = None     
            messages = await resp.json() 
            
    for message in messages:
        # print(message)
        if(message['content'] != ""):
            match = re.search(urlRegexImage, message['content'])
            print(match)
            if(match):
                return message['content']
        if(len(message['attachments']) > 0):
            if('url' in message['attachments'][0].keys()):
                return message['attachments'][0]['url']
    return None