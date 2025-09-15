from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

class image:
    @staticmethod
    def generate(charact, text):
        try:
            font = ImageFont.truetype("arial.ttf", 40)
        except:
            font = ImageFont.load_default()

        img = Image.open("assets/TRUMP.jpg")
        draw = ImageDraw.Draw(img)

        position = (260, 230)   # координаты текста
        color = (0, 0, 0)     # черный текст

        draw.text(position, text, fill=color, font=font)

        img_buffer = BytesIO()
        img.save(img_buffer, format="JPEG")
        img_buffer.seek(0)

        return img_buffer
