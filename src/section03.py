"""
Wikipediaの記事を以下のフォーマットで書き出したファイルjawiki-country.json.gzがある．
* 1行に1記事の情報がJSON形式で格納される
* ファイル全体はgzipで圧縮される
* 各行には記事名が"title"キーに，記事本文が"text"キーの辞書オブジェクトに格納され，そのオブジェクトがJSON形式で書き出される

以下の処理を行うプログラムを作成せよ．
"""

import gzip
import json
import os
import re
# import sys


def get_data_dir_path():
    data_dir = os.path.join(os.path.dirname(__file__), "..", "data")
    section_dir = os.path.join(data_dir, "section03")
    os.makedirs(section_dir, exist_ok=True)
    return section_dir


def load_wiki() -> list:
    """
    Returns
    =======
    contents: list
    """
    data_dir = get_data_dir_path()
    wiki_gz_path = os.path.join(data_dir, "jawiki-country.json.gz")
    try:
        with gzip.open(wiki_gz_path, 'rb') as fp:
            wiki_content_raw = fp.read().decode('utf-8')
    except Exception as error:
        print(f"ERROR: load_wiki(). error={error}")
    wiki_raw_contents = wiki_content_raw.replace('\r\n', '\n').split('\n')
    wiki_contents = []
    for idx, wiki_raw_content in enumerate(wiki_raw_contents):
        try:
            wiki_content = json.loads(wiki_raw_content)
        except Exception as error:
            print(f"WARN: Load json error. idx={idx}, error={error}, len(raw_content)={len(wiki_raw_content)}")
            continue
        wiki_contents.append(wiki_content)
    return wiki_contents


def get_country_desctiption(contents, country):
    desctiption = ""
    for content in contents:
        if 'title' not in content.keys():
            continue
        if 'text' not in content.keys():
            continue
        if country in content['title']:
            text = content['text']
            text_lines = text.split('\n')
            desctiption = text_lines
    return desctiption


def section03_20():
    """
    20. JSONデータの読み込み
    Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．
    問題21-29では，ここで抽出した記事本文に対して実行せよ．
    """
    contents = load_wiki()
    desctiption = get_country_desctiption(contents, 'イギリス')
    data_dir = get_data_dir_path()
    with open(os.path.join(data_dir, 'england.txt'), 'w', encoding='utf-8') as fp:
        fp.write('\n'.join(desctiption))
    print('\n'.join(desctiption[:3]) + "...")
    return desctiption


def section03_21():
    """
    21. カテゴリ名を含む行を抽出
    記事中でカテゴリ名を宣言している行を抽出せよ．
    """
    contents = load_wiki()
    desctiption = get_country_desctiption(contents, 'イギリス')
    pattern = r"\[\[Category:.*\]\]"
    category_lines = []
    for line in desctiption:
        if re.search(pattern, line) is not None:
            category_lines.append(line)
    result = '\n'.join(category_lines)
    print(result)
    return result


def section03_22():
    """
    22. カテゴリ名の抽出
    記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．
    """
    contents = load_wiki()
    desctiption = get_country_desctiption(contents, 'イギリス')
    pattern = r"\[\[Category:(.*)\]\]"
    category_names = []
    for line in desctiption:
        match = re.search(pattern, line)
        if match is not None:
            category_name = match.group(1)
            category_names.append(category_name)
    result = '\n'.join(category_names)
    print(result)
    return result


def section03_23():
    """
    23. セクション構造
    記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ．
    """
    contents = load_wiki()
    desctiption = get_country_desctiption(contents, 'イギリス')
    pattern_lv1 = r"^==([^\=]+)=="
    pattern_lv2 = r"^===([^\=]+)==="
    section_pair_list = []
    for line in desctiption:
        match_lv1 = re.search(pattern_lv1, line)
        match_lv2 = re.search(pattern_lv2, line)
        if match_lv1 is not None:
            section_name = match_lv1.group(1)
            section_pair_list.append((1, section_name))
        elif match_lv2 is not None:
            section_name = match_lv2.group(1)
            section_pair_list.append((2, section_name))
    result = '\n'.join([f"{item[0]}, {item[1]}" for item in section_pair_list])
    print(result)
    return result


def section03_24():
    """
    24. ファイル参照の抽出
    記事から参照されているメディアファイルをすべて抜き出せ．
    """
    pass


def section03_25():
    """
    25. テンプレートの抽出
    記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ．
    """
    pass


def section03_26():
    """
    26. 強調マークアップの除去
    25の処理時に，テンプレートの値からMediaWikiの強調マークアップ（弱い強調，強調，強い強調のすべて）を除去してテキストに変換せよ
    （参考: マークアップ早見表）．
    """
    pass


def section03_27():
    """
    27. 内部リンクの除去
    26の処理に加えて，テンプレートの値からMediaWikiの内部リンクマークアップを除去し，テキストに変換せよ（参考: マークアップ早見表）．
    """
    pass


def section03_28():
    """
    28. MediaWikiマークアップの除去
    27の処理に加えて，テンプレートの値からMediaWikiマークアップを可能な限り除去し，国の基本情報を整形せよ．
    """
    pass


def section03_29():
    """
    29. 国旗画像のURLを取得する
    テンプレートの内容を利用し，国旗画像のURLを取得せよ．
    （ヒント: MediaWiki APIのimageinfoを呼び出して，ファイル参照をURLに変換すればよい）
    """
    pass


if __name__ == '__main__':
    try:
        func_list = [
            section03_20,
            section03_21,
            section03_22,
            section03_23,
            section03_24,
            section03_25,
            section03_26,
            section03_27,
            section03_28,
            section03_29,
        ]
        for func in func_list:
            print(f"== START {func} ==")
            func()
    except Exception as e:
        print(f"ERROR error={e}")
