# histimeline

`histimeline` は、歴史上の出来事を日付順に並べるコマンドです。
歴史のノート整理や、社会科のレポート作成に利用できます。

## 特徴

- 入力された出来事を古い順に並べ替える
- 標準入力からデータを受け取る
- Markdown形式で標準出力へ出力する
- 間違った入力をエラーとして知らせる

## 動作環境

- Python 3.9以上
- Linux、macOS、WindowsのUbuntu環境など

外部ライブラリは使用しません。

## 入力形式

1行につき、日付と出来事をタブで区切って入力します。

```text
YYYY-MM-DD<TAB>出来事

## 年で絞り込む

`--year` を使うと、指定した年の出来事だけ表示できます。

```bash
cat examples/events.txt | python3 histimeline.py --year 1945
