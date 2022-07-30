#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Webスクレイピング用プログラムである。
"""

__author__ = 'Kobayashi Shun'
__version__ = '1.0.0'
__date__ = '2022/7/26 (Created: 2022/07/26)'

from tkinter.messagebox import NO
from bs4 import BeautifulSoup
import requests


def main():
    morse_table = table_of_katakana_and_morse(
        "http://www1.odn.ne.jp/haru/data-list/morse.html")
    if morse_table is None:
        return 1


def table_of_katakana_and_morse(the_url_string):
    """
    モールス信号のWebページをウェブスクレイピングし、カタカナとモールス信号の辞書を作って応答します。
    抽出できない場合には、Noneを応答します。
    """
    response = requests.get(the_url_string)
    if response.status_code != 200:
        return None

    response.encoding = response.apparent_encoding
    html_source = response.text

    # print(html_source)

    beautiful_soup = BeautifulSoup(html_source, 'html.parser')

    table_set = beautiful_soup.find_all(
        name='table')
    tr_set = table_set.

    print(table_set)

    return None


def generate_table(table_set):
    """
    渡されたtableから組み込みアイテムとハイパーリンクの辞書を作って応答します。
    抽出できない場合には、Noneを応答します。
    """
    dictionary = {}
    for div_an_item in table_set:
        a_tag = div_an_item.find(name='a', attrs={'class': tag_name})
        if a_tag is not None:
            builtin_function = a_tag.string.strip()
            hyper_reference = the_url_string.replace(
                'index.html', '') + a_tag['href']
            # print('"{}" : "{}"'.format(builtin_function, hyper_reference))

            table[builtin_function] = hyper_reference


if __name__ == '__main__':
    import sys
    sys.exit(main())
