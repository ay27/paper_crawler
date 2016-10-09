# Created by ay27 at 16/10/8
import os, sys
from conference import *
from journal import *
from multiprocessing import Process


def read_config(file_path, type_str):
    with open(file_path, encoding='utf-8') as f:
        result = []
        flag = False
        for line in f:
            if len(line) < 2:
                continue
            line = line.strip()
            if line.startswith('[') and line.endswith(']'):
                if line == '[%s]' % type_str:
                    flag = True
                else:
                    flag = False
                continue
            if flag:
                result.append(line)
    return result


def main1(keyword):
    conference_list = read_config('config.ini', 'conference')
    for conf in conference_list:
        craw_conference(conf, keyword)


def main2(keyword):
    journal_list = read_config('config.ini', 'journal')
    for journal in journal_list:
        craw_journal(journal, keyword)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: paper_crawler keyword')
        exit(1)

    keyword = sys.argv[1]
    p1 = Process(target=main1, args=(keyword,))
    p1.start()

    p2 = Process(target=main2, args=(keyword,))
    p2.start()

    p1.join()
    p2.join()
