"""
hightemp.txtは，日本の最高気温の記録を「都道府県」「地点」「℃」「日」のタブ区切り形式で格納したファイルである．
以下の処理を行うプログラムを作成し，hightemp.txtを入力ファイルとして実行せよ．
さらに，同様の処理をUNIXコマンドでも実行し，プログラムの実行結果を確認せよ．
"""

import os
import sys


def get_data_dir_path():
    data_dir = os.path.join(os.path.dirname(__file__), "..", "data")
    return data_dir


def load_hightemp() -> str:
    """
    Returns
    =======
    texts: str
    """
    here = os.path.dirname(__file__)
    file_path = os.path.join(here, "..", "data", "hightemp.txt")
    try:
        with open(file_path, 'r', encoding='utf-8') as fp:
            texts = fp.read()
    except Exception as error:
        print(error)
        raise error

    lines = texts.replace('\r\n', '\n').split('\n')
    last_line = lines[-1].strip('\r\n')
    if len(last_line) == 0:
        lines = lines[:-1]
    return lines


def section02_10():
    """
    10. 行数のカウント
    行数をカウントせよ．確認にはwcコマンドを用いよ．
    """
    lines = load_hightemp()
    line_count = len(lines)
    print(line_count)
    return line_count


def section02_11():
    """
    11. タブをスペースに置換
    タブ1文字につきスペース1文字に置換せよ．
    確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．
    """
    lines = load_hightemp()
    new_lines = []
    for line in lines:
        new_line = line.replace('\t', ' ')
        new_lines.append(new_line)
    result = '\n'.join(new_lines)
    print(result)
    return result


def section02_12():
    """
    12. 1列目をcol1.txtに，2列目をcol2.txtに保存
    各行の1列目だけを抜き出したものをcol1.txtに，
    2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．
    確認にはcutコマンドを用いよ．
    """
    lines = load_hightemp()
    col1_lines = []
    col2_lines = []
    for line in lines:
        cols = line.split('\t')
        if len(cols) >= 1:
            col1_lines.append(cols[0])
            if len(cols) >= 2:
                col2_lines.append(cols[1])
    print(f"col1_lines={col1_lines}")
    print(f"col2_lines={col2_lines}")
    data_dir = get_data_dir_path()
    with open(os.path.join(data_dir, "col1.txt"), 'w', encoding='utf-8') as fp:
        fp.writelines([line + '\n' for line in col1_lines])
    with open(os.path.join(data_dir, "col2.txt"), 'w', encoding='utf-8') as fp:
        fp.writelines([line + '\n' for line in col2_lines])
    return col1_lines, col2_lines


def section02_13():
    """
    13. col1.txtとcol2.txtをマージ
    12で作ったcol1.txtとcol2.txtを結合し，
    元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．
    確認にはpasteコマンドを用いよ．
    """
    data_dir = get_data_dir_path()
    with open(os.path.join(data_dir, "col1.txt"), 'r', encoding='utf-8') as fp:
        col1_lines = fp.readlines()
    with open(os.path.join(data_dir, "col2.txt"), 'r', encoding='utf-8') as fp:
        col2_lines = fp.readlines()
    combine_lines = []
    for col1, col2 in zip(col1_lines, col2_lines):
        combine_lines.append('\t'.join([col1.strip(), col2.strip()]))
    result = '\n'.join(combine_lines)
    print(result)
    return result


def section02_14():
    """
    # 14. 先頭からN行を出力
    # 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．
    # 確認にはheadコマンドを用いよ．
    """
    N = int(sys.argv[1])
    lines = load_hightemp()
    result = '\n'.join(lines[:N])
    print(f"N = {N}")
    print(result)
    return result


def section02_15():
    """
    15. 末尾のN行を出力
    自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．
    確認にはtailコマンドを用いよ．
    """
    N = int(sys.argv[1])
    lines = load_hightemp()
    result = '\n'.join(lines[-N:])
    print(f"N = {N}")
    print(result)
    return result


def section02_16():
    """
    16. ファイルをN分割する
    自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．
    同様の処理をsplitコマンドで実現せよ．
    """
    N = int(sys.argv[1])
    lines = load_hightemp()
    line_count = len(lines)
    chunk_size = int(line_count / N)
    chunks = []
    for idx in range(N):
        chunk_head = chunk_size * idx
        chunk = lines[chunk_head:(chunk_head + chunk_size)]
        chunks.append('\n'.join(chunk))
    for idx, chunk in enumerate(chunks):
        print(f"# chunk_idx = {idx}")
        print(chunk)
    return chunks


def section02_17():
    """
    17. １列目の文字列の異なり
    1列目の文字列の種類（異なる文字列の集合）を求めよ．
    確認にはsort, uniqコマンドを用いよ．
    """
    lines = load_hightemp()
    col1_lines = []
    for line in lines:
        cols = line.split('\t')
        if len(cols) >= 1:
            col1_lines.append(cols[0])
    col1_set = set(col1_lines)
    result = f"num = {len(col1_set)}, unique items = {sorted(list(col1_set))}"
    print(result)
    return len(col1_set)


def section02_18():
    """
    18. 各行を3コラム目の数値の降順にソート
    各行を3コラム目の数値の逆順で整列せよ
    （注意: 各行の内容は変更せずに並び替えよ）．確認にはsortコマンドを用いよ
    （この問題はコマンドで実行した時の結果と合わなくてもよい）．
    """
    lines = load_hightemp()
    cols_lines = []
    for line in lines:
        cols = line.split('\t')
        if len(cols) >= 3:
            item = (cols[2], line)
            cols_lines.append(item)
        else:
            print(f"ERROR: col={cols[2]}, line={line}")
    new_lines = sorted(cols_lines, key=lambda x: x[0], reverse=True)
    result = '\n'.join([item[1] for item in new_lines])
    print(result)
    return result


def section02_19():
    """
    19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
    各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．
    確認にはcut, uniq, sortコマンドを用いよ．
    """
    lines = load_hightemp()
    col1_bow = {}
    for line in lines:
        cols = line.split('\t')
        if len(cols) >= 1:
            col1 = cols[0]
            if col1 not in col1_bow.keys():
                col1_bow[col1] = 0
            col1_bow[col1] += 1
    col1_bow_list = [(word, count) for word, count in col1_bow.items()]
    col1_bow_list = sorted(col1_bow_list, key=lambda x: x[1], reverse=True)
    result = '\n'.join([f"{item[1]} {item[0]}" for item in col1_bow_list])
    print(result)
    return result


if __name__ == '__main__':
    try:
        func_list = [
            section02_10,
            section02_11,
            section02_12,
            section02_13,
            section02_14,
            section02_15,
            section02_16,
            section02_17,
            section02_18,
            section02_19,
        ]
        for func in func_list:
            print(f"== START {func} ==")
            func()
    except Exception as e:
        print(f"ERROR error={e}")
