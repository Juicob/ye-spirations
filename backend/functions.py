import json
import random
import requests
from unsplash.api import Api
from unsplash.auth import Auth
from PIL import Image, ImageDraw, ImageFont 

with open('../secrets.json') as f:
    d = json.load(f)
    auth = Auth(client_id=d['unsplash']['client_id'], client_secret=d['unsplash']['client_secret'], redirect_uri=d['unsplash']['redirect_uri'], code=None)
    
api = Api(auth)

def get_rando_line():
    with open(r'../data/Kanye West Lyrics.txt', encoding='utf8') as f:
        lines = f.readlines()
        not_blank_or_descriptive_lines = [line for line in lines if len(line) > 1 and '[' not in line]
        rando_line = not_blank_or_descriptive_lines[random.randrange(0,len(not_blank_or_descriptive_lines))]
        print(rando_line)
        return rando_line
    
def get_rando_photo(search_term, orientation='landscape'):
    request = api.photo.random(1, query=search_term, orientation=orientation)[0].urls.regular
    response = requests.get(request, stream=True)
    response.raw.decode_content = True
    rando_photo = Image.open(response.raw) #.convert("RGBA")
    return rando_photo

def put_line_on_photo(rando_line, photo, text_size=30):
    print(rando_line, photo)
    font_type = ImageFont.load_default()#.truetype(font='arial.ttf', size=text_size)
    draw = ImageDraw.Draw(photo)
    draw.text(xy=(50,150), 
         text=rando_line, 
         fill=(150,105,150,50), 
         font=font_type)
    return photo
