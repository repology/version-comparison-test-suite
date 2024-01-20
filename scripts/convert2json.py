#!/usr/bin/env python3

import json
import re
from sys import argv, stdin


ALLOWED_FLAGS = set('palu')


def read_input() -> str:
    if len(argv) > 1:
        with open(argv[1]) as f:
            return f.read()
    return stdin.read()


res = {'sections':[]}
current_section = None

for lineno, line in enumerate(read_input().splitlines()):
    if m := re.fullmatch('\[(.*)\]', line):
        if current_section is None or current_section['name'] != m[1]:
            current_section = {
                'name': m[1],
                'testcases': [],
            }
            res['sections'].append(current_section)
    elif m := re.fullmatch('"(.*)" ([a-zA-Z]*)([<>=])([a-zA-Z]*) "(.*)"', line):
        if current_section is None:
            raise RuntimeError('test case outside of section')
        current_section['testcases'].append({
            'left_version': m[1],
            'left_flags': m[2],
            'expected_result': m[3],
            'right_flags': m[4],
            'right_version': m[5],
        })
    elif line and not line.startswith('#'):
        raise RuntimeError(f'unexpected input at line {line}')

print(json.dumps(res, indent='  '))
