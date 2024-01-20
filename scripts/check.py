#!/usr/bin/env python3

import re
from sys import argv, exit, stdin


ALLOWED_FLAGS = set('palu')


def report_error(lineno: int, message: str) -> None:
    print(f'Line {lineno}: {message}')
    exit(1)


def is_quoted(string: str) -> bool:
    return string.startswith('"') and string.endswith('"')


def read_input() -> str:
    if len(argv) > 1:
        with open(argv[1]) as f:
            return f.read()
    return stdin.read()


known_sections = set()

for lineno, line in enumerate(read_input().splitlines(), start=1):
    if line.startswith('#'):
        pass  # comment
    elif not line:
        pass  # empty
    elif line.startswith('['):
        if not line.endswith(']'):
            report_error(lineno, 'section name not closed')
        section_name = line[1:-1]
        if section_name in known_sections:
            report_error(lineno, f'duplicate section name {section_name}')
        known_sections.add(section_name)
    else:
        comps = line.split(' ')
        if len(comps) != 3:
            report_error(lineno, 'expected test case in <version1> <operator> <version2> format')
        if not is_quoted(comps[0]) or not is_quoted(comps[2]):
            report_error(lineno, 'version string not quoted')

        operator_comps = re.split('[<>=]', comps[1])
        if len(operator_comps) != 2:
            report_error(lineno, 'invalid comparison relation')

        for flag in ''.join(operator_comps):
            if flag not in ALLOWED_FLAGS:
                report_error(lineno, 'invalid comparison flag "{flag}"')
