import os
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import time
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

def download_video(url):
    response = requests.get(url, verify=True)
    with open("video.mp4", "wb") as f:
        f.write(response.content)

    soup = BeautifulSoup(response.content, 'html.parser')

    video_tag = soup.find('video', {'class': 'video-stream'})
    if video_tag is None:
        print('Could not find video tag on page.')
        return

    video_url = video_tag['src']

    file_name = os.path.basename(video_url)

    response = requests.get(video_url, stream=True, verify=True)

    chunk_size = 1024

    total_size = int(response.headers.get('content-length', 0))

    progress_bar = tqdm(total=total_size, unit='iB', unit_scale=True)

    start_time = time.time()
    with open(file_name, 'wb') as f:
        for chunk in response.iter_content(chunk_size):
            if chunk:
                f.write(chunk)
                progress_bar.update(len(chunk))
    
    download_speed = total_size / (time.time() - start_time) / 1024 / 1024
    print(f'\nDownload speed: {download_speed:.2f} MB/s')

    progress_bar.close()

    print(f'{file_name} downloaded successfully.')

url = 'https://www.sample-videos.com/video123/mp4/720/big_buck_bunny_720p_1mb.mp4'
download_video(url)
