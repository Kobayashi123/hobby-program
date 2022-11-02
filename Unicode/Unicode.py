
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Unicode変換プログラム：文字列をUnicodeに変換して表示します。
"""

__author__ = 'Kobayashi Shun'
__version__ = '0.0.0'
__date__ = '2022/11/01 (Created: 2022/11/01)'

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

        unicode_line = input_str.encode('unicode-escape')
        print("Unicode: " + str(unicode_line)[2:-1])
        # print(type(byte_line))

        utf8_line = input_str.encode('utf-8')
        print("UTF-8: " + str(utf8_line)[2:-1].replace('\\x', '%'))
        # print(utf8_line.hex())
        # print(type(utf8_line))

        shift_jis_line = input_str.encode('shift-jis')
        print("Shift-JIS: " + str(shift_jis_line)[2:-1].replace('\\x', '%'))
        # print(type(shiftJIS_line))

        str_line = unicode_line.decode('unicode-escape')
        print("Unicode -> 文字列: " + str_line)
        # print(type(str_line))

    return 0

if __name__ == '__main__':  # ifによって、このスクリプトファイルが直接実行されたときだけ、以下の部分を実行する。
    import sys
    # このモジュールのmain()を呼び出して結果を得て、Pythonシステムに終わりを告げる。
    sys.exit(main())
