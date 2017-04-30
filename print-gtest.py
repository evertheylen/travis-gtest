#!/usr/bin/env python3

import sys
import os
import xml.etree.ElementTree as ET

#from termcolor import colored
# Copy-paste:
ATTRIBUTES = dict(list(zip(
    ['bold', 'dark', '','underline', 'blink', '', 'reverse', 'concealed'],
    list(range(1, 9)))))
del ATTRIBUTES['']

HIGHLIGHTS = dict(list(zip(
    ['on_grey', 'on_red', 'on_green', 'on_yellow', 'on_blue', 'on_magenta', 'on_cyan', 'on_white'],
     list(range(40, 48)))))

COLORS = dict(list(zip(
    ['grey', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white'],
     list(range(30, 38)))))

RESET = '\033[0m'

def colored(text, color=None, on_color=None, attrs=None):
    if os.getenv('ANSI_COLORS_DISABLED') is None:
        fmt_str = '\033[%dm%s'
        if color is not None:
            text = fmt_str % (COLORS[color], text)

        if on_color is not None:
            text = fmt_str % (HIGHLIGHTS[on_color], text)

        if attrs is not None:
            for attr in attrs:
                text = fmt_str % (ATTRIBUTES[attr], text)

        text += RESET
    return text

# End of termcolor.colored


index_to_status = {i: status for i, status in 
            enumerate(['notrun', 'run', 'error', 'fault'])}
status_to_index = {v: k for k,v in index_to_status.items()}

colors = {
    'notrun': 'grey',
    'run': 'green',
    'error': 'yellow',
    'fault': 'red',
}

symbols = {
    'notrun': '/',
    'run': '✓',
    'error': '!',
    'fault': 'X',
}

colored_symbols = {k: colored(sym, colors[k], attrs=['bold'])
                   for k, sym in symbols.items()}

# Slight modifications for text
colors['notrun'] = None

def status_index(el):
    if el.tag.lower() == 'testcase':
        return status_to_index[el.attrib['status']]
    else:
        return max(status_index(i) for i in el)


def print_el(el, depth=0, maxdepth=3):
    name = el.attrib['name']
    indent = '  ' + depth*'  '
    if el.tag.lower() == 'testcase':
        stat = el.attrib['status']
        print(indent + colored_symbols[stat] + ' ' + colored(name, colors[stat]))
    else:
        stat = index_to_status[status_index(el)]
        s = indent + colored_symbols[stat] + ' ' + colored(name, colors[stat])
        if depth+1 >= maxdepth:
            s += ' [' + ' '.join(colored_symbols[index_to_status[status_index(c)]]
                    for c in el) + ']'
            print(s)
        else:
            print(s)
            for child in el:
                print_el(child, depth=depth+1, maxdepth=maxdepth)


if len(sys.argv) <= 1:
    print("Not enough arguments. Usage: print.py <filename>")
    sys.exit(1)

tree = ET.parse(sys.argv[1])
print_el(tree.getroot())


