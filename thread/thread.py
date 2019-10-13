from flask import Flask, render_template

from contextlib import contextmanager
import concurrent.futures
import requests
import os
import time


app = Flask(__name__)


@contextmanager
def change_dir(dest):
    """ Change dir where we need to download images to, so that to render them in index.html and then change dir back to the root."""

    try:
        cwd = os.getcwd()
        os.chdir(dest)
        yield
    finally:
        os.chdir(cwd)


# Just two images so far, but then we will increase the number to 10 or 15
img_urls = [
    'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759',
    'https://images.unsplash.com/photo-1532009324734-20a7a5813719'
]


def download_img(img_url):
    """ Take img_url, save the content of the image and then write bytes of the content into destination folder """

    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[3]
    img_name = f'{img_name}.jpg'
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)


static = 'static'
start = time.perf_counter()

with change_dir(static):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(download_img, img_urls)

finish = time.perf_counter()

finished = round((finish - start), 2)

result = {
    'source': 'https://www.imgix.com/',
    'number_of_images': len(img_urls),
    'time_to_download': finished
}


@app.route('/')
def show_index():
    return render_template("index.html", result=result)


@app.route('/time')
def show_time():
    return result


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1000, debug=True)
