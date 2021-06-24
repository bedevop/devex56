# AS-3, Igal
import time
from PIL import Image, ImageDraw, ImageFont

file_name = '_' + str(int(time.time())) + '_file.png'
img = Image.new('RGB', (500, 200), color=(73, 109, 137))

font = ImageFont.truetype('./ttf/wintersong.ttf', 64)
d = ImageDraw.Draw(img)
d.text((10, 10), "DevEx20210506", font=font, fill=(255, 255, 0))

img.save(file_name)

