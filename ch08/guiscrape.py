# Rejurhf
# 18.10.2018

from tkinter import ttk, filedialog, messagebox
import base64
import json
import os
from bs4 import BeautifulSoup
import requests

if __name__ == "__main__":
    _root = Tk()
    _root.title('Scrape app')
    _mainframe = ttk.Frame(_root, padding='5 5 5 5')
    _mainframe.grid(row=0, column=0, sticky=(E,W,N,S))
    _url_frame = ttk.LabelFrame(_mainframe, text='URL', padding='5 5 5 5')
    _url_frame.grid(row=0, column=0, sticky=(E,W))
    _url_frame.columnconfigure(0, weight=1)
    _url_frame.rowconfigure(0, weight=1)
    _url = StringVar()
    _url.set('http://localhost8000')
    _url_entry = ttk.Entry(_url_frame, width=40, textvariable=_url)
    _url_entry.grid(row=0, column=0, sticky=(E, W, S, N), padx=5)
    _fetch_btn = ttk.Button(_url_frame, text='Fetch info', command=fetch_url)
    _fetch_btn.grid(row=0, column, sticky=W, padx=5)

    parser = argparse.ArgumentParser(description='Scrape a webpage.')
    parser.add_argument('-t', '--type', choices=['all', 'png', 'jpg'],
        default='all', help='The image type we want to scrape.')
    parser.add_argument('-f', '--format', choices=['img', 'json'],
        default='img', help='The format images are saved to.')
    parser.add_argument('url', help='The URL we want to scrape for images.')
    args = parser.parse_args()
    scrape(args.url, args.format, args.type)
