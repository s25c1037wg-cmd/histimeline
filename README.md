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
```

## 出力例

```text
- 1600-10-21：関ヶ原の戦い
- 1945-08-15：終戦
```

## エラー

入力形式が間違っている場合、エラーを標準エラー出力へ表示します。

## テスト

```bash
$ python3 -m unittest -v
```

## 作者

Yusuke Kimura

## ライセンス

MIT License

Copyright (c) 2026 Yusuke Kimura
