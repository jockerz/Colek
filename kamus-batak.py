#!/usr/bin/python3
import argparse

import requests
from bs4 import BeautifulSoup
from requests.exceptions import ConnectionError

URL = 'https://www.kamusbatak.com/kamus'
NOT_FOUND_TEXT = 'Belum ada terjemahan :( '\
                 'Dang adong dope terjemahan bahh :('

http = requests.Session()
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) '\
                  'Gecko/20100101 Firefox/78.0'
    }


def do_request(url_args):
    try:
        resp = http.post(URL, params=url_args, headers=HEADERS)
        resp.raise_for_status()
        return resp.text
    except ConnectionError:
        print(" Connection failed")


def _process(elem_panel):
    strong = elem_panel.find('strong')
    italic = elem_panel.find('i')
    if strong and italic:
        print(f' ▶️ {strong.string.strip()}')
        print(f'   {italic.string.strip()}')
    else:
        print(f' ▶️ {elem_panel.string.strip()}')


def parse_html(html_text):
    soup = BeautifulSoup(html_text, 'html.parser')
    panels = soup.find_all('div', class_='panel panel-default')
    is_first = True
    for panel in panels:
        panel = panel.div
        if is_first:
            is_first = False
            print(f' ◼️ {panel.string.strip()}\n')
            continue
        _process(panel)


def main():
    parser = argparse.ArgumentParser(
        description='Kamus Bahasa Batak - Indonesia dan sebaliknya')
    parser.add_argument('words', metavar='Word(s)', action="store", nargs="+",
                        help='Kata / kalimat yang ingin di terjemahkan')
    parser.add_argument('-i', action='store_true', default=False, dest='reverse',
                        help="Bahasa Indonesia - Batak")
    args = vars(parser.parse_args())

    bahasa = 'indonesia' if args.get('reverse') else 'batak'

    if isinstance(args['words'], list):
        text = ' '.join(args['words'])
    else:
        text = args['words']
    url_args = {
        'teks': text, 'bahasa': bahasa,
        'submit': 'LIHAT HASIL TERJEMAHAN'
    }

    html = do_request(url_args)
    if html is None:
        return

    if NOT_FOUND_TEXT in html:
        print(f' {NOT_FOUND_TEXT}')
    else:
        result = parse_html(html)


if __name__ == '__main__':
    main()


