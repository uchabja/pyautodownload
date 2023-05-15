# -*- coding: utf-8 -*-
import requests
import os

def download_file(url):
    local_filename = url.split('/')[-1] # get the file name
    try:
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(local_filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192): 
                    f.write(chunk)
        print(f'Downloaded: {url}')
        return local_filename
    except Exception as e:
        print(f'Failed to download {url}. Reason: {e}')
        return None

def main():
    # Please replace with your text file path
    text_file_path = "links.txt"

    with open(text_file_path, 'r', encoding='utf8') as file:
        urls = file.read().splitlines() # read the file and split lines into a list

    for url in urls:
        download_file(url)

if __name__ == "__main__":
    main()
