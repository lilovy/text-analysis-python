import glob
from PIL import Image


def create_gif(gifname: str,
               fold: str):
    images = []


    files = glob.glob(f"{fold}\*.png")

    for i in files:
        new_frame = Image.open(i)
        images.append(new_frame)

    images[0].save(f'{fold}\{gifname}.gif', save_all=True, duration=1500,
                   append_images=images[1:], loop=0)