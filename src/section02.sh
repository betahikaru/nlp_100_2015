# section02

# hightemp.txtは，日本の最高気温の記録を「都道府県」「地点」「℃」「日」のタブ区切り形式で格納したファイルである．
# 以下の処理を行うプログラムを作成し，hightemp.txtを入力ファイルとして実行せよ．
# さらに，同様の処理をUNIXコマンドでも実行し，プログラムの実行結果を確認せよ．
data_dir=`dirname $0`/../data
file_path=${data_dir}/hightemp.txt

# 10. 行数のカウント
# 行数をカウントせよ．確認にはwcコマンドを用いよ．
echo No.10
cat ${file_path} | wc -l

# 11. タブをスペースに置換
# タブ1文字につきスペース1文字に置換せよ．
# 確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．
echo No.11
cat ${file_path} | tr '\t' ' '

# 12. 1列目をcol1.txtに，2列目をcol2.txtに保存
# 各行の1列目だけを抜き出したものをcol1.txtに，
# 2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．
# 確認にはcutコマンドを用いよ．
echo No.12
cat ${file_path} | tr '\t' ' ' | cut -d' ' -f 1 > ${data_dir}/col1.txt
cat ${file_path} | tr '\t' ' ' | cut -d' ' -f 2 > ${data_dir}/col2.txt
head ${data_dir}/col1.txt
head ${data_dir}/col2.txt

# 13. col1.txtとcol2.txtをマージ
# 12で作ったcol1.txtとcol2.txtを結合し，
# 元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．
# 確認にはpasteコマンドを用いよ．
echo No.13
paste ${data_dir}/col1.txt ${data_dir}/col2.txt

# 14. 先頭からN行を出力
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．
# 確認にはheadコマンドを用いよ．
echo No.14
num=${1}
cat ${file_path} | head -n ${num}

# 15. 末尾のN行を出力
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．
# 確認にはtailコマンドを用いよ．
echo No.15
num=${1}
cat ${file_path} | tail -n ${num}

# 16. ファイルをN分割する
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．
# 同様の処理をsplitコマンドで実現せよ．
echo No.16
num=${1}
split -l ${num} ${file_path} ${data_dir}/no16_split_prefix_
ls ${data_dir}/no16_split_prefix_*

# 17. １列目の文字列の異なり
# 1列目の文字列の種類（異なる文字列の集合）を求めよ．
# 確認にはsort, uniqコマンドを用いよ．
echo No.17
cat ${file_path} | cut -f 1 | sort | uniq | wc -l

# 18. 各行を3コラム目の数値の降順にソート
# 各行を3コラム目の数値の逆順で整列せよ
# （注意: 各行の内容は変更せずに並び替えよ）．確認にはsortコマンドを用いよ
# （この問題はコマンドで実行した時の結果と合わなくてもよい）．
cat ${file_path} | sort -n -r

# 19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
# 各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．
# 確認にはcut, uniq, sortコマンドを用いよ．
echo No.19
cat ${file_path} | cut -f 1 | sort | uniq -c | sort -r

