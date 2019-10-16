from flask import Flask, render_template
from flask_restful import Resource, Api

from contextlib import contextmanager
import concurrent.futures
import requests
import os
import time

from PIL import Image, ImageFilter


app = Flask(__name__)
api = Api(app)


@contextmanager
def change_dir(dest):
    """ Change dir where we need to download images to, so that to render them in index.html and then change dir back to the root."""

    try:
        cwd = os.getcwd()
        os.chdir(dest)
        yield
    finally:
        os.chdir(cwd)


img_urls = [
    'https://images.unsplash.com/photo-1530224264768-7ff8c1789d79',
    'https://images.unsplash.com/photo-1564135624576-c5c88640f235',
    'https://images.unsplash.com/photo-1541698444083-023c97d3f4b6',
    'https://images.unsplash.com/photo-1522364723953-452d3431c267',
    'https://images.unsplash.com/photo-1513938709626-033611b8cc03',
    'https://images.unsplash.com/photo-1507143550189-fed454f93097',
    'https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e'

    # 'https://images.unsplash.com/photo-1504198453319-5ce911bafcde',
    # 'https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99',
    # 'https://images.unsplash.com/photo-1516972810927-80185027ca84',
]


def download_img(img_url):
    """ Take img_url, save the content of the image and then write bytes of the content into destination folder """

    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[3]
    img_name = f'{img_name}.jpg'
    images.append(img_name)
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)


images = []
static = 'static'
start = time.perf_counter()

with change_dir(static):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(download_img, img_urls)

finish = time.perf_counter()

finished = round((finish - start), 2)


def process_image(img_name):
    img = Image.open(f'static/{img_name}')

    img = img.filter(ImageFilter.GaussianBlur(15))

    img.thumbnail(size)
    img.save(f'static/processed/{img_name}')


size = (300, 300)
start2 = time.perf_counter()

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(process_image, images)


finish2 = time.perf_counter()

finished2 = round((finish2 - start2), 2)

result = {
    'source': 'https://www.imgix.com/',
    'number_of_images': len(img_urls),
    'time_to_download': finished,
    'time_to_resize': finished2,
    'images': images
}


class Results(Resource):
    def get(self):
        return {
            'results': [result]
        }


api.add_resource(Results, '/data')


@app.route('/')
def show_index():
    return render_template("index.html", result=result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1000, debug=True)
