# encoding:utf8
import os
import sys
import datetime


def write_all_text(path: str, text: str):
    with open(path, 'w', encoding='utf-8')as f:
        f.write(text)


def get_text(title: str):
    d = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    s = f'''---
title: {title}
date: {d}
---
'''
    return s


if __name__ == "__main__":
    date = datetime.datetime.now().strftime('%Y-%m-%d-')
    title = input('please input title\n')
    path = os.path.join(os.path.split(sys.path[0])[
                        0], 'source', '_posts', f'{date}{title}.md')
    write_all_text(path, get_text(title))
