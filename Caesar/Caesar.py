#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
入力された英文をCaesar暗号で暗号化するプログラムである。
簡易的に作ったため、クラスは使っていない。ライブラリとして使えるように、クラスを使って作り直すことを検討する。
"""

__author__ = 'Kobayashi Shun'
__version__ = '0.0.0'
__date__ = '2022/10/03 (Created: 2022/10/02)'

def encrypt(input_string, key) -> str:
    """
    input_stringをCaesar暗号で暗号化します。keyで与えられた数だけ文字をずらします。
    Returns:
        str: 暗号化した文字列
    """
    cipher_str = ''
    for char in input_string:
        if char.isalpha():
            # Encrypt uppercase characters in plain text
            if char.isupper():
                cipher_str += chr((ord(char) - 65 + key) % 26 + 65)
            # Encrypt lowercase characters in plain text
            else:
                cipher_str += chr((ord(char) - 97 + key ) % 26 + 97)
        else:
            cipher_str += char
    return cipher_str

def decrypt(input_string, key) -> str:
    """
    input_stringをCaesar暗号で復号化します。keyで与えられた数だけ文字をずらします。
    Returns:
        str: 復号化した文字列
    """
    plain_str = ''
    for char in input_string:
        if char.isalpha():
            # Encrypt uppercase characters in plain text
            if char.isupper():
                plain_str += chr((ord(char) - 65 - key) % 26 + 65)
            # Encrypt lowercase characters in plain text
            else:
                plain_str += chr((ord(char) - 97 - key) % 26 + 97)
        else:
            plain_str += char
    return plain_str

def main():
    """
    Caesar暗号で暗号化するメイン（main）プログラムです。
    常に0を応答します。それが結果（リターンコード：終了ステータス）になることを想定しています。
    """
    print("Caesar暗号で暗号化する文を入力してください。")
    print("終了する場合は、Ctrl + D または exit, quit を入力してください。")
    print()

    mode = 1
    mode_choice = input("Which mode do you want to use? (Encrypt: 1, Decrypt: 2): ")
    if mode_choice == '1':
        mode = 1
    elif mode_choice == '2':
        mode = 2

    key = int(input("input cipher key (1~26): "))
    print()

    print('----------------------------------------')
    if mode == 1:
        print('--------  Encrypt Mode Selected  -------')
    else:
        print('--------  Decrypt Mode Selected  -------')
    print('----------  Shift pattern ' + str(key) + '  -----------')
    print('----------------------------------------')

    while True:
        try:
            input_string = input(">> ")
            if input_string in ('exit', 'quit'):
                break
        except EOFError:
            print()
            break
        if mode == 1:
            print('Cipher:  ' + encrypt(input_string, key))
        elif mode == 2:
            print('Plain:  ' + decrypt(input_string, key))
    return 0

if __name__ == '__main__':  # ifによって、このスクリプトファイルが直接実行されたときだけ、以下の部分を実行する。
    import sys
    # このモジュールのmain()を呼び出して結果を得て、Pythonシステムに終わりを告げる。
    sys.exit(main())
