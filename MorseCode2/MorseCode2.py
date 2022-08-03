#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
入力された文をモールス信号に変換するプログラムである。
"""

__author__ = 'Kobayashi Shun'
__version__ = '1.3.0'
__date__ = '2022/08/03 (Created: 2022/07/25)'

import MeCab as mecab
from PIL import Image


class MorseCode2:
    """
    入力された文をモールス信号に変換する。
    """

    def __init__(self, text):
        """
        インスタンスを生成します。
        """
        self._original_string = text
        self._reading = ''
        self._morse_message = ''

    def get_reading(self) -> str:
        """
        カタカナの読みを返す

        Returns:
            _reading: カタカナ文
        """
        return self._reading

    def get_morse(self) -> str:
        """
        モールス信号を返す

        Returns:
            _morse: モールス信号
        """
        return self._morse_message

    def pronunciation(self):
        """
        文を受け取り、その読み方をカタカナに変換して出力する。

        Returns:
                String: 受け取った文字列の読み方をカタカナで返す
        """
        m = mecab.Tagger()

        result = m.parse(self._original_string).splitlines()  # mecabの解析結果の取得
        result = result[:-1]  # EOFの排除

        for vocabulary in result:
            if '\t' not in vocabulary:
                continue
            # surface = vocabulary.split('\t')[0]  # 表層系を取得
            ruby = vocabulary.split('\t')[1].split(',')[-2]  # ルビ(読み方)を取得
            self._reading += ruby

        self.dakuon_transfer()
        self.shouon_transfer()

    def dakuon_transfer(self):
        """
        濁点・半濁点を変換する
        """
        dakuonpu_dictionary = {'ガ': 'カ゛', 'ギ': 'キ゛', 'グ': 'ク゛', 'ゲ': 'ケ゛', 'ゴ': 'コ゛',
                               'ザ': 'サ゛', 'ジ': 'シ゛', 'ズ': 'ス゛', 'ゼ': 'セ゛', 'ゾ': 'ソ゛',
                               'ダ': 'タ゛', 'ヂ': 'チ゛', 'ヅ': 'ツ゛', 'デ': 'テ゛', 'ド': 'ト゛',
                               'バ': 'ハ゛', 'ビ': 'ヒ゛', 'ブ': 'フ゛', 'ベ': 'ヘ゛', 'ボ': 'ホ゛',
                               'パ': 'ハ゜', 'ピ': 'ヒ゜', 'プ': 'フ゜', 'ペ': 'ヘ゜', 'ポ': 'ホ゜',
                               }
        list_of_dakuonpu = dakuonpu_dictionary.keys()
        list_of_dakuonpu = list(list_of_dakuonpu)
        for char in list_of_dakuonpu:
            if char in self._reading:
                self._reading = self._reading.replace(
                    char, dakuonpu_dictionary.get(char))

    def shouon_transfer(self):
        """
        拗音を変換する
        """
        shouon_dictionary = {'ッ': 'ツ', 'ャ': 'ヤ', 'ュ': 'ユ', 'ョ': 'ヨ'}
        list_of_shouon = shouon_dictionary.keys()
        list_of_shouon = list(list_of_shouon)
        for char in list_of_shouon:
            if char in self._reading:
                self._reading = self._reading.replace(
                    char, shouon_dictionary.get(char))

    def string_to_morse(self):
        """
        カタカナ文を受け取り、モールス信号変換して出力する。
        """
        morse_dictionary = {'ア': '--.--', 'イ': '.-', 'ウ': '..-', 'エ': '-.---', 'オ': '.-...',
                            'カ': '.-..', 'キ': '-.-..', 'ク': '...-', 'ケ': '-.--', 'コ': '----',
                            'サ': '-.-.-', 'シ': '--.-.', 'ス': '---.-', 'セ': '.---.', 'ソ': '---.',
                            'タ': '-.', 'チ': '..-.', 'ツ': '.--.', 'テ': '.-.--', 'ト': '..-..',
                            'ナ': '.-.', 'ニ': '-.-.', 'ヌ': '....', 'ネ': '--.-', 'ノ': '..--',
                            'ハ': '-...', 'ヒ': '--..-', 'フ': '--..', 'ヘ': '.', 'ホ': '-..',
                            'マ': '-..-', 'ミ': '..-.-', 'ム': '-', 'メ': '-...-', 'モ': '-..-.',
                            'ヤ': '.--', 'ユ': '-..--', 'ヨ': '--',
                            'ラ': '...', 'リ': '--.', 'ル': '-.--.', 'レ': '---', 'ロ': '.-.-',
                            'ワ': '-.-', 'ヲ': '.---', 'ン': '.-.-.',
                            'ー': '.--.-', '、': '.-.-.-', '゛': '..', '゜': '..--.'
                            }
        for char in self._reading:
            try:
                self._morse_message += morse_dictionary[char] + " "
            except KeyError:
                print('\" ' + char + ' " is not in Morse Dictionary.')

    def generate_animation_code(self) -> str:
        """
        モールス信号のアニメーションコードを作成する

        Returns:
            signals: モールス信号のコード
        """
        # 「.は_3個+空白2個、-は_6個+空白 2個。単語間は空白6個」に変換
        code_to_signal = {'.': '___' + '  ',
                          '-': '_________' + '  ', ' ': '       '}  # 継続時間補正
        is_signal_on = {'_': True, ' ': False}  # 時系列ON/OFF信号用

        # 文字列をモールス符号文字列に変換し、"."と"_"の継続時間
        time_codes = ''.join([code_to_signal[m] for m in self._morse_message])
        signals = [is_signal_on[char] for char in time_codes]

        return signals


def generate_animation(signals):
    """
    モールス信号のアニメーションコードを元にアニメーションを作成し、gifファイルに保存する
    """
    # モールス符号の信号がONなら「白画像」、OFFなら「黒画像」にするためのテーブル
    w = 600
    h = 1200
    image = {True: Image.new('RGB', (w, h), (255, 255, 255)),
             False:  Image.new('RGB', (w, h), (0, 0, 0))}
    images = [image[s] for s in signals]
    images[0].save('message.gif', save_all=True,
                   append_images=images[1:], optimize=True, duration=100, loop=10)


def main():
    """
    入力された文をモールス信号に変換するプログラムです。
    常に0を応答します。それが結果（リターンコード：終了ステータス）になることを想定しています。
    """
    print("モールス信号に変換する文を入力してください")
    print("Ctrl&D または exit, quit を入力することで実行を終わります")
    print()

    animation_code_list = []
    while True:
        try:
            input_str = input('> ')
            if input_str in ('exit', 'quit'):
                break
        except EOFError:
            print()
            break

        morse = MorseCode2(input_str)
        morse.pronunciation()
        morse.string_to_morse()
        print(input_str)
        print(morse.get_reading())
        print(morse.get_morse())
        animation_code_list.append(morse.generate_animation_code())
        print()

    for an_animation_code in animation_code_list:
        generate_animation(an_animation_code)

    return 0


if __name__ == '__main__':  # このスクリプトファイルが直接実行されたときだけ、以下の部分を実行する。
    import sys
    # MorseCode2モジュールのmain()を呼び出して結果を得て、Pythonシステムに終わりを告げる。
    sys.exit(main())
