import random


def section01_00():
    """
    00. 文字列の逆順
    文字列"stressed"の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．
    """
    result = "".join(reversed("stressed"))
    print(result)
    return result


def section01_01():
    """
    01. 「パタトクカシーー」
    「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．
    """
    base = "パタトクカシーー"
    result = ""
    for idx in range(len(base)):
        if (idx + 1) % 2 == 1:
            result += base[idx]
    print(result)
    return result


def section01_02():
    """
    02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
    「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
    """
    base1 = "パトカー"
    base2 = "タクシー"
    result = ""
    for ch1, ch2 in zip(base1, base2):
        result += ch1 + ch2
    print(result)
    return result


def section01_03():
    """
    03. 円周率
    "Now I need a drink, alcoholic of course,
     after the heavy lectures involving quantum mechanics."
    という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．
    """
    base = "Now I need a drink, alcoholic of course,"
    base += " after the heavy lectures involving quantum mechanics."
    result = ""
    for word in base.split(" "):
        result += f"{len(word)}"
    print(result)
    return result


def section01_04():
    """
    04. 元素記号
    "Hi He Lied Because Boron Could Not Oxidize Fluorine.
     New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，
    それ以外の単語は先頭に2文字を取り出し，取り出した文字列から単語の位置（先頭から何番目の単語か）への
    連想配列（辞書型もしくはマップ型）を作成せよ．
    """
    base = "Hi He Lied Because Boron Could Not Oxidize Fluorine."
    base += " New Nations Might Also Sign Peace Security Clause."
    base += " Arthur King Can."
    result = {}
    for idx, word in enumerate(base.split(" ")):
        if (idx + 1) in [1, 5, 6, 7, 8, 9, 15, 16, 19]:
            result[idx] = word[:1]
        else:
            result[idx] = word[:2]
    print(result)
    return result


def bi_gram(base_list):
    return n_gram(base_list, 2)


def n_gram(base_list, n):
    result_list = []
    for pos in range(len(base_list) - n + 1):
        result_list.append(base_list[pos:pos + n])
    return result_list


def section01_05():
    """
    05. n-gram
    与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
    この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．
    """
    base = "I am an NLPer"
    result_words = n_gram(base.split(" "), 2)
    result_chara = n_gram(base, 2)
    print(result_words)
    print(result_chara)
    return result_words, result_chara


def section01_06():
    """
    06. 集合
    "paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，
    それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．
    さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．
    """
    base1 = "paraparaparadise"
    base2 = "paragraph"
    X = set(bi_gram(base1))
    Y = set(bi_gram(base2))
    X_or_Y = X | Y
    X_and_Y = X & Y
    X_diff_Y = X - Y
    print("section01_06")
    print(base1, base2)
    print(f"X or Y:      {X_or_Y}")
    print(f"X and Y:     {X_and_Y}")
    print(f"X diff Y:    {X_diff_Y}")
    print(f"X have 'se': {'se' in X}")
    print(f"Y have 'se': {'se' in Y}")
    return X, Y


def section01_07():
    """
    07. テンプレートによる文生成
    引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．
    さらに，x=12, y="気温", z=22.4として，実行結果を確認せよ．
    """
    def template(x, y, z):
        result = f"{x}時の{y}は{z}"
        return result

    result = template(12, "気温", 22.4)
    print(result)
    return result


def section01_08():
    """
    08. 暗号文
    与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．

    英小文字ならば(219 - 文字コード)の文字に置換
    その他の文字はそのまま出力
    この関数を用い，英語のメッセージを暗号化・復号化せよ．
    """
    def cipher(x):
        """
        ord(chara: str) -> int
        chr(code: int) -> str

        % python -c "print(97, 122, 219 - 97, 219 - 122)"
        97 122 122 97
        """
        result = ""
        for ch in x:
            code = ord(ch)
            if code >= 97 and code <= 122:
                result += chr(219 - code)
            else:
                result += ch
        return result

    base = "This is cipher."
    print(f"base:    {base}")
    cipher1 = cipher(base)
    print(f"cipher1: {cipher1}")
    cipher2 = cipher(cipher(base))
    print(f"cipher2: {cipher2}")
    return base, cipher1, cipher2


def section01_09():
    """
    09. Typoglycemia
    スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，
    それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
    ただし，長さが４以下の単語は並び替えないこととする．
    適当な英語の文（例えば"I couldn't believe that I could actually understand
     what I was reading : the phenomenal power of the human mind ."）を与え，
    その実行結果を確認せよ．
    """
    base = "I couldn't believe that I could actually understand"
    base += " what I was reading : the phenomenal power of the human mind ."
    result = ""
    for word in base.split(" "):
        if len(word) <= 4:
            result += word + " "
            continue
        else:
            new_word = word[0]
            center = [word[idx] for idx in range(1, len(word) - 1)]
            random.shuffle(center)
            new_word += "".join(center)
            new_word += word[-1]
            result += new_word + " "
    print(f"base:   {base}")
    print(f"result: {result}")
    return result


if __name__ == '__main__':
    try:
        func_list = [
            section01_00,
            section01_01,
            section01_02,
            section01_03,
            section01_04,
            section01_05,
            section01_06,
            section01_07,
            section01_08,
            section01_09,
        ]
        for func in func_list:
            print(f"== START {func} ==")
            func()
    except Exception as e:
        print(f"ERROR error={e}")
