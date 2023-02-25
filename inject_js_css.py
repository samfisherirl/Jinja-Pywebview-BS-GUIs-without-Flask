# This script is used to combine all css and js files in the directory
# and its subdirectories into a single file (index.html)
# It will also place all css and js at the bottom of the page,
# which is useful for loading pages.
#
# It will also create a backup of the original index.html file,
# and replace the original with the new one.
#
#
#
# This script is used in conjunction with the flask framework.
# It is designed to be run from the command line in the directory
# where the index.html file is located.
#
#
#
# The script will look for and use the following markers in the index.html file:
#
# <HEAD> </HEAD>  - for css insertion
# <BODY> </B
import os
from os import getcwd
from os.path import exists, join, getsize
from time import sleep
from pathlib import Path 
from settings import file_settings


Files = file_settings()

css_paths = []
js_paths = []

lookfor_css = r"</head>"
lookfor_js = r"</body>"

# Use these literal markers as places for respective cod3e
# DO NOT include <script> <style> for insert markers, these will be added for
# marker locations. use outside of this is fine.

# assign directory 

filename = 'index.html'

log = Files.log
# iterate over files in
# that directory


def find_css_js_files():
    for file in Files.dir.rglob("*"):
        print(file) 
        if file.suffix == ".css":
            css_paths.append(file)
        if file.suffix  == ".js":
            js_paths.append(file)


def read_file_return_contents(file):
    with open(file, 'r', errors='ignore') as f:
        return f.read()


def read_js(line):
    js = f"\n<script>\n"
    for file in js_paths:
        js = str(js + read_file_return_contents(file))
    return str(js + f"\n</script>\n" + line)


def read_css(line):
    css = f"\n<style>\n"
    for file in css_paths:
        css = str(css + read_file_return_contents(file))
    return str(css + f"\n</style>\n" + line)


def find_larger_size(): 
    backupsize = Path(Files.bpath).stat().st_size
    fsize = Path(Files.fpath).stat().st_size
    
    if (int(backupsize) > int(fsize)):
        return Files.fpath
    else:
        return Files.bpath


def read_index_html():
    file = find_larger_size() 
    with open(Files.fpath, 'r', errors="replace") as f:
        export = f.read()
        html_lines = export.split('\n')
    # save backup of original
    with open(Files.bpath, 'w') as f:
        f.write(export)
    return html_lines


def access_directory():
    return read_file_return_contents(Files.log)


# def save_directory(path, file):
#     with open(log, 'w') as f:
#         f.write(f'{path},{file}')


def restore_backup():
    file = read_file_return_contents(Files.bpath)
    with open(Files.fpath, 'w',
            errors="ignore") as f:
        f.write(file)


def insert_js_css(html_lines):
    new_html = []
    for line in html_lines:
        if lookfor_css in line:
            new_html.append(read_css(line))  # insert css on marker
            continue
        elif lookfor_js in line:
            new_html.append(read_js(line))  # insert js on marker
            continue
        else:
            new_html.append(line)
    return new_html


def convert(Files):
    directory = Files.dir
    find_css_js_files()
    html_lines = read_index_html()
    new_html = insert_js_css(html_lines)
    with open(Files.fpath, 'w', errors="replace") as f:
        f.write("\n".join(new_html))


if __name__ == '__main__':
    convert(Files)
    sleep(2)
    restore_backup()
