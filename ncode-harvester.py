#!/usr/bin/env python3

import sys
import os
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

if len(sys.argv) < 4:
    sys.exit("Not enough argument, usage: harvester novel_index_url start_chapter end_chapter")

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0',
}

cookies = {
    'over18':'yes'
}

savePath = "extractedFiles"

def get_page(url):
    try:
        with closing(get(url, headers=headers, stream=True, cookies=cookies)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error("Error during request to {0} : {1}".format(url, str(e)))
        return None


def is_good_response(resp):
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)


def log_error(e):
    print(e)


def get_subtitle(html):
    subtitle = ""
    for p in html.select("p.novel_subtitle"):
        subtitle = p.text
    return subtitle


def novel_content(html):
    content = ""
    for div in html.select("div#novel_honbun"):
        content = div.text
    return content


url = (sys.argv[1])
ch0 = (sys.argv[2])
chx = (sys.argv[3])

for ch in range(int(ch0), int(chx) + 1):
    raw_html = get_page(url + str(ch))
    html = BeautifulSoup(raw_html, "html.parser")
    print("Downloading chapter " + str(ch) + " - " + html.title.string)
    fileTitle = str(ch).zfill(3) + "_" + get_subtitle(html) + ".txt"
    with open(os.path.join(savePath,fileTitle), "w", encoding="utf-8") as text_file:
        print(f"{novel_content(html)}", file=text_file)