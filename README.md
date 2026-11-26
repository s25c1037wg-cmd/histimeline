# histimeline

`histimeline` は、歴史上の出来事を日付順に整理するコマンドです。
社会科のノート整理やレポート作成に利用できます。

## 特徴

- 日付の古い順に表示
- `--reverse` で新しい順に表示
- `--year` で指定した年だけ表示
- `--keyword` でキーワード検索
- 標準入力から読み取り、標準出力へ結果を出力
- 入力エラーは標準エラー出力へ表示

## 動作環境

- Ubuntu 24.04
- Python 3.12
- 外部ライブラリ不要

## 入力形式

1行につき、日付と出来事をタブで区切ります。

```text

YYYY-MM-DD<TAB>出来事
$ cat examples/events.txt | python3 histimeline.py
$ cat examples/events.txt | python3 histimeline.py --reverse
$ cat examples/events.txt | python3 histimeline.py --year 1945
$ cat examples/events.txt | python3 histimeline.py --keyword 戦い
