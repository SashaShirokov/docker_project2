import numpy as np
from matplotlib import pyplot as plt
import requests
import json


r_t = requests.get('http://0.0.0.0:1010/data')
r_m = requests.get('http://0.0.0.0:3010/data')


result_t = json.loads(r_t.content)
result_m = json.loads(r_m.content)

plt.style.use('fivethirtyeight')

# comic style...
# plt.xkcd()

type = ['threading', 'multiprocessing']

x_indexes = np.arange(len(type))
width = 0.2

resize = [result_t['results'][0]['time_to_resize'], result_m['results'][0]['time_to_resize']]
download = [result_t['results'][0]['time_to_download'], result_m['results'][0]['time_to_download']]


plt.bar(x_indexes + width, resize, width=width, color='#00ffff', label='Resize')
plt.bar(x_indexes, download, width=width,  color='#9f9fff', label='Download')


plt.xticks(ticks=x_indexes, labels=type)

plt.xlabel('downloading and resizing ' +
           str(result_m['results'][0]['number_of_images']) + ' image(s)...')
plt.ylabel('Time(seconds)')
plt.title('Threading vs MultiProcessing')

plt.legend()

plt.tight_layout()

plt.show()
