#!/usr/bin/env python
# -*- coding: utf-8 -*-

from morse3 import Morse as morse
from PIL import Image
import MeCab as mecab

# 「.は_3個+空白2個、-は_6個+空白 2個。単語間は空白6個」に変換
CODE_TO_SIGNAL = {'.': '___  ', '-': '______  ', ' ': '      '}  # 継続時間補正用
IS_SIGNAL_ON = {'_': True, ' ': False}  # 時系列ON/OFF信号用

# 文字列をモールス符号文字列に変換し、"."と"_"の継続時間
mouse_message = morse('Yes').stringToMorse()
time_codes = ''.join([CODE_TO_SIGNAL[m] for m in mouse_message])
signals = [IS_SIGNAL_ON[c] for c in time_codes]

# モールス符号として表示したり、時系列ON/OFF信号を表示したり
print(mouse_message)
print(time_codes)

# モールス符号の信号がONなら「白画像」、OFFなら「黒画像」にするためのテーブル
w = 600
h = 1200
IMAGE = {True: Image.new('RGB', (w, h), (255, 255, 255)),
         False:  Image.new('RGB', (w, h), (0, 0, 0))}
images = [IMAGE[s] for s in signals]
images[0].save('message.gif', save_all=True,
               append_images=images[1:], optimize=True, duration=100, loop=10)
