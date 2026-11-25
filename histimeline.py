#!/usr/bin/env python3

import sys
from datetime import date


def read_events(lines):
    events = []

    for line_number, line in enumerate(lines, start=1):
        line = line.rstrip("\n")

        if not line.strip():
            continue

        try:
            date_text, event = line.split("\t", 1)
            date.fromisoformat(date_text)
        except ValueError:
            print(
                f"入力エラー: {line_number}行目は"
                " YYYY-MM-DD<TAB>出来事 の形式で入力してください",
                file=sys.stderr,
            )
            continue

        events.append((date_text, event.strip()))

    return sorted(events)


def main():
    events = read_events(sys.stdin)

    for date_text, event in events:
        print(f"- {date_text}：{event}")


if __name__ == "__main__":
    main()
