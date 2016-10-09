# Created by ay27 at 16/10/8
import os, sys
from conference import *
from journal import *

result_file = 'result.md'


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


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: paper_crawler keyword')
        exit(1)

    keyword = sys.argv[1]

    journal_list = read_config('config.ini', 'journal')
    for journal in journal_list:
        volumes = craw_journal(journal, keyword)
        with open(result_file, 'a') as f:
            f.write('# %s\n' % journal)
        for volume in volumes:
            write_journal(volume[0], volume[1], volume[3])

    conference_list = read_config('config.ini', 'conference')
    for conf in conference_list:
        workshops = craw_conference(conf, keyword)
        with open(result_file, 'a') as f:
            f.write('# %s\n' % conf)
        for workshop in workshops:
            write_conference(workshop[0], workshop[1])
