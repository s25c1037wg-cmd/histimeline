# Copyright (c) 2026 Yusuke Kimura
# SPDX-License-Identifier: MIT
#!/usr/bin/env python3

import argparse
import sys
from datetime import date


def read_events(lines, target_year=None, reverse=False, keyword=None):
    events = []

    for line_number, line in enumerate(lines, start=1):
        line = line.rstrip("\n")

        if not line.strip():
            continue

        try:
            date_text, event = line.split("\t", 1)
            parsed_date = date.fromisoformat(date_text)
        except ValueError:
            print(
                f"入力エラー: {line_number}行目は"
                " YYYY-MM-DD<TAB>出来事 の形式で入力してください",
                file=sys.stderr,
            )
            continue

        event = event.strip()

        if target_year is not None and parsed_date.year != target_year:
            continue

        if keyword is not None and keyword not in event:
            continue

        events.append((parsed_date, event))

    return sorted(events, reverse=reverse)


def main():
    parser = argparse.ArgumentParser(
        description="歴史上の出来事を検索・並べ替えします"
    )

    parser.add_argument(
        "--year",
        type=int,
        help="指定した年の出来事だけ表示します",
    )

    parser.add_argument(
        "--reverse",
        action="store_true",
        help="新しい出来事から表示します",
    )

    parser.add_argument(
        "--keyword",
        help="出来事に含まれるキーワードで検索します",
    )

    args = parser.parse_args()
    events = read_events(
        sys.stdin,
        target_year=args.year,
        reverse=args.reverse,
        keyword=args.keyword,
    )

    for event_date, event in events:
        print(f"- {event_date.isoformat()}：{event}")


if __name__ == "__main__":
    main()
