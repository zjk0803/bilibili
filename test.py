import requests


def download_file(url, path):
    with requests.get(url, stream=True) as r:
        chunk_size = 1024
        content_size = int(r.headers['content-length'])
        print("下载开始")
        with open(path, "wb") as f:
            for chunk in r.iter_content(chunk_size=chunk_size):
                f.write(chunk)


if __name__ == '__main__':
    url = 'https://www.bilibili.com/video/av52916699/'
    path = 'D:'
    download_file(url, path)