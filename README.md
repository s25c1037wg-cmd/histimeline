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
## キーワードで検索する

`--keyword` を使うと、出来事に指定した文字列が含まれるものだけ表示できます。

```bash
printf "1600-10-21\t関ヶ原の戦い\n1945-08-15\t終戦\n1868-01-03\t王政復古の大号令\n" | python3 histimeline.py --keyword 戦い
