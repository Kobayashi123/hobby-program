#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
入力された文をモールス信号に変換するプログラムである。
"""

__author__ = 'Kobayashi Shun'
__version__ = '1.0.0'
__date__ = '2022/7/29 (Created: 2022/07/25)'

import MeCab as mecab


class MorseCode2:
    """
    入力された文をモールス信号に変換する。
    """

    string = None

    reading = ''

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

    dakuonpu_dictionary = {'ガ': 'カ゛', 'ギ': 'キ゛', 'グ': 'ク゛', 'ゲ': 'ケ゛', 'ゴ': 'コ゛',
                           'ザ': 'サ゛', 'ジ': 'シ゛', 'ズ': 'ス゛', 'ゼ': 'セ゛', 'ゾ': 'ソ゛',
                           'ダ': 'タ゛', 'ヂ': 'チ゛', 'ヅ': 'ツ゛', 'デ': 'テ゛', 'ド': 'ト゛',
                           'バ': 'ハ゛', 'ビ': 'ヒ゛', 'ブ': 'フ゛', 'ベ': 'ヘ゛', 'ボ': 'ホ゛',
                           'パ': 'ハ゜', 'ピ': 'ヒ゜', 'プ': 'フ゜', 'ペ': 'ヘ゜', 'ポ': 'ホ゜',
                           }

    def __init__(self, text):
        """
        インスタンスを生成します。
        """
        self.string = text

    def get_pronunciation(self, text):
        """文を受け取り、その読み方をカタカナに変換して出力する。

        Args:
                text (String): 文

        Returns:
                String: 受け取った文字列の読み方をカタカナで返す
        """
        m = mecab.Tagger()

        print(self.string)

        result = m.parse(self.string).splitlines()  # mecabの解析結果の取得
        result = result[:-1]  # EOFの排除

        for vocabulary in result:
            if '\t' not in vocabulary:
                continue
            # surface = vocabulary.split('\t')[0]  # 表層系を取得
            ruby = vocabulary.split('\t')[1].split(',')[-2]  # ルビ(読み方)を取得
            self.reading += ruby

        print('reading: ' + self.reading)

        self.reading = self.dakuon_transfer(self.reading)

        return self.reading

    def dakuon_transfer(self, a_string):
        """濁点・半濁点を変換する
        Args:
                list (_type_): _description_
        Returns:
                _type_: _description_
        """
        print('aString: ' + a_string)
        list_of_dakuonpu = self.dakuonpu_dictionary.keys()
        list_of_dakuonpu = list(list_of_dakuonpu)
        for char in list_of_dakuonpu:
            if char in a_string:
                a_string = a_string.replace(
                    char, self.dakuonpu_dictionary.get(char))

        return a_string

    def string_to_morse(self, text):
        """カタカナ文を受け取り、モールス信号変換して出力する。

        Args:
                text (String): カタカナ文

        Returns:
                String: モールス信号
        """
        answer = ""
        for char in text:
            try:
                answer += self.morse_dictionary[char] + "   "
            except KeyError:
                print('\" ' + char + ' " is not in Morse Dictionary.')

        return answer


def main():
    """
    入力された文をモールス信号に変換するプログラムです。
    常に0を応答します。それが結果（リターンコード：終了ステータス）になることを想定しています。
    """
    input_str = input("モールス信号に変換する文を入力してください: ")
    morse = MorseCode2(input_str)

    reading = morse.get_pronunciation(input_str)
    print(reading)
    answer = morse.string_to_morse(reading)
    print(answer)

    return 0


if __name__ == '__main__':  # このスクリプトファイルが直接実行されたときだけ、以下の部分を実行する。
    import sys
    # MorseCode2モジュールのmain()を呼び出して結果を得て、Pythonシステムに終わりを告げる。
    sys.exit(main())
