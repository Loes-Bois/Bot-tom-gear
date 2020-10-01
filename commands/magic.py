# import the necessary packages
import numpy as np
from urllib.request import urlopen
import cv2
import io
import aiohttp
import discord
import matplotlib.pyplot as plt
import math

# METHOD #1: OpenCV, NumPy, and urllib
async def url_to_image(url):
	# download the image, convert it to a NumPy array, and then read
	# it into OpenCV format
    print(url)
    resp = await get_url(url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)

    # return the image
    return image

async def main(self, message):

    message_parts = message.content.split(" ")

    url = message.attachments[0].url if len(message.attachments) > 0 else False

    # if no attachment check for embeddeds
    url = message.embeds[0].url if len(message.embeds) > 0 else url

    url = message_parts[2] if (len(message_parts)) > 2 else url
    
    if(url):
        data = await url_to_image(url)

        magic_image_data = make_magic(data)

        bits = bts_to_img(magic_image_data)

        f = io.BytesIO(bits)
        attachment = discord.File(f , 'cool_image.png')

        await message.channel.send(file=attachment)
    else:
        await message.channel.send("I would like an image please :D")

#await channel.send(file=discord.File(data, 'cool_image.png'))

async def get_url(url):
    data = None
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status != 200:
                return await channel.send('Could not download file...')
            data = io.BytesIO(await resp.read())
            return data
    return data    


def make_magic(image):
    
    warp = wrap_image(image)

    return warp

def bts_to_img(bts):
    '''
    :param bts: results from image_to_bts
    '''
    ret, img = cv2.imencode('.png', bts)
    return np.array(img).tostring()

def wrap_image(img):
    """
    apply the wrap to images
    """
    rows,cols,ch = img.shape
    print(img.shape)
    pts1 = np.float32([[1,3],[rows,3],[1,cols],[rows,cols]])
    pts2 = np.float32([[0,0],[rows,0],[0,cols],[rows,cols]])

    M = cv2.getPerspectiveTransform(pts1,pts2)

    image_wraped = cv2.warpPerspective(img, M, (cols, rows))
    
    edges = cv2.Canny(image_wraped,cols,rows)

    edges = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

    dst = cv2.addWeighted(edges, 0.2, image_wraped, 0.8, 0.3)

    dst = vertical_wave(dst)
    
    # pts1 = np.float32([[50,50],[200,50],[50,200]])
    # pts2 = np.float32([[10,100],[200,50],[100,250]])

    # M = cv2.getAffineTransform(pts1,pts2)

    # dst = cv2.warpAffine(image_wraped,M,(cols,rows))

    plt.figure()
    plt.imshow(dst)
    plt.show()
    
    return dst



def vertical_wave(img):
    #####################
    # Vertical wave

    rows, cols,ch = img.shape
    img_output = np.zeros(img.shape, dtype=img.dtype)

    for i in range(rows):
        for j in range(cols):
            offset_x = int(25.0 * math.sin(2 * 3.14 * i / 180))
            offset_y = 0
            if j+offset_x < rows:
                img_output[i,j] = img[i,(j+offset_x)%cols]
            else:
                img_output[i,j] = 0
    return img_output

def horizontal_wave(img):
    #####################
    # Horizontal wave
    
    rows, cols,ch = img.shape
    img_output = np.zeros(img.shape, dtype=img.dtype)

    for i in range(rows):
        for j in range(cols):
            offset_x = 0
            offset_y = int(16.0 * math.sin(2 * 3.14 * j / 150))
            if i+offset_y < rows:
                img_output[i,j] = img[(i+offset_y)%rows,j]
            else:
                img_output[i,j] = 0


def hor_vert_wave(img):
    #####################
    # Both horizontal and vertical 
    rows, cols,ch = img.shape
    img_output = np.zeros(img.shape, dtype=img.dtype)

    for i in range(rows):
        for j in range(cols):
            offset_x = int(20.0 * math.sin(2 * 3.14 * i / 150))
            offset_y = int(20.0 * math.cos(2 * 3.14 * j / 150))
            if i+offset_y < rows and j+offset_x < cols:
                img_output[i,j] = img[(i+offset_y)%rows,(j+offset_x)%cols]
            else:
                img_output[i,j] = 0
    return img_output


def concave_wave(img):
    #####################
    # Concave effect

    rows, cols,ch = img.shape
    img_output = np.zeros(img.shape, dtype=img.dtype)

    for i in range(rows):
        for j in range(cols):
            offset_x = int(128.0 * math.sin(2 * 3.14 * i / (2*cols)))
            offset_y = 0
            if j+offset_x < cols:
                img_output[i,j] = img[i,(j+offset_x)%cols]
            else:
                img_output[i,j] = 0

    return image_output