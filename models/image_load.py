import numpy as np
from urllib.request import urlopen
import cv2
import io
import aiohttp

async def url_to_image(url, message):
    '''
    Obtains the image and convert it into mutatable opencv matrix
    '''

    resp = await get_url(url, message)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)

    # return the image
    return image

async def get_url(url, message):
    '''
    Grabs Image from URL using discord reccomdations
    '''
    data = None
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status != 200:
                return await message.channel.send('Could not download file...')
            data = io.BytesIO(await resp.read())
            return data
    return data  


def bts_to_img(bts):
    '''
    Convert matix of value into byte array
    '''
    ret, img = cv2.imencode('.png', bts)
    return np.array(img).tostring()