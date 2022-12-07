#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Unicode変換プログラム：文字列をUnicodeに変換して表示します。
"""

__author__ = 'Kobayashi Shun'
__version__ = '1.0.0'
__date__ = '2022/12/06 (Created: 2022/11/01)'

def main():
    """
    文字列をUnicodeに変換するメイン（main）プログラムです。
    常に0を応答します。それが結果（リターンコード：終了ステータス）になることを想定しています。
    """

    print("Unicodeに変換する文字列を入力してください")
    print("Ctrl&D または exit, quit を入力することで実行を終わります")
    print()

    while True:
        try:
            input_str = input('> ')
            if input_str in ('exit', 'quit'):
                break
        except EOFError:
            print()
            print("終了します")
            break

        unicode_line = encode_unicode(input_str)
        print("Unicode: " + str(unicode_line)[2:-1].replace('\\\\u', ' '))

        utf8_line = encode_utf8(input_str)
        utf8_line = str(utf8_line)[2:-1].replace('\\x', '%')
        print("UTF-8: " + utf8_line)
        utf8_line = utf8_line.replace('%', ' ')
        print("UTF-8 hex: " + utf8_line)
        utf8_list = utf8_line.split(' ')[1:]
        for i in range(len(utf8_list)):
            utf8_list[i] = bin(int(utf8_list[i], 16))[2:]
        print("UTF-8 bin: " + ' '.join(utf8_list))

    return 0

def encode_unicode(input_str: str) -> bytes:
    """
    文字列をUnicodeに変換します。
    """
    unicode_line = input_str.encode('unicode-escape')
    return unicode_line

def encode_utf8(input_str: str) -> bytes:
    """
    文字列をUTF-8に変換します。
    """
    utf8_line = input_str.encode('utf-8')
    return utf8_line

def encode_shift_jis(input_str: str) -> bytes:
    """
    文字列をShift-JISに変換します。
    """
    shift_jis_line = input_str.encode('shift_jis')
    return shift_jis_line

def decode_unicode(input_str: bytes) -> str:
    """
    Unicodeを文字列に変換します。
    """
    str_line = input_str.decode('unicode-escape')
    return str_line

def decode_utf8(input_str: bytes) -> str:
    """
    UTF-8を文字列に変換します。
    """
    str_line = input_str.decode('utf-8')
    return str_line

def decode_shift_jis(input_str: bytes) -> str:
    """
    Shift-JISを文字列に変換します。
    """
    str_line = input_str.decode('shift_jis')
    return str_line

if __name__ == '__main__':  # ifによって、このスクリプトファイルが直接実行されたときだけ、以下の部分を実行する。
    import sys
    # このモジュールのmain()を呼び出して結果を得て、Pythonシステムに終わりを告げる。
    sys.exit(main())
