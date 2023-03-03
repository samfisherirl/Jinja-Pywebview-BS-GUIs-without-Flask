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
# <BODY> </B>
from os import remove

import html
import minify_html

import os
from os import getcwd
from os.path import exists, getsize
from time import sleep
from pathlib import Path

try:
    from templates.settings import file_settings
    from templates.class_construction import Tag, Paths, Html
except:
    from settings import file_settings
    from class_construction import Tag, Paths, Html

Files = file_settings()

css_paths = []
js_paths = []

Html = Html()


# Use these literal markers as places for respective cod3e
# DO NOT include <script> <style> for insert markers, these will be added for
# marker locations. use outside of this is fine.

# assign directory 

filename = 'index.html'

log = Files.log

js = Paths('\n<script>\n', "\n</script>\n", r"</body>")
css = Paths('\n<style>\n', "\n</style>\n", r"</head>")


            
def writer(name, content):
    with open(name, 'w', encoding='utf-8', errors="replace") as f:
        f.write(content)


# iterate over files in
# that directory


def read_file_(file):
    with open(file, 'r', errors='replace', encoding='utf-8') as f:
        return str(f.read())


def read_js_css(line, scriptor, paths):
    for file in js_paths:
        pass


def css_search(line):
        if css.lookfor_ in line:
            css.construction()
            return True
        else:
            Html.header_(line)
            return False

def js_search(line):
        if js.lookfor_ in line:
            js.construction()
            return True
        else:
            Html.body_(line)
            return False



def get_file_size(filename):
    try:
        return Path(filename).stat().st_size
    except:
        return 0


# The code then checks if there are any files with a size greater than 100000 bytes, and if so it deletes them.
# If the terminal is closed without saving, the backup is not restored. To ensure doubling of injection, it 
# will clean the index file, as well  as leave markers on the index file as breadcrums


def minify_(code):
    return minify_html.minify(code, minify_js=False, remove_processing_instructions=False)


def access_directory():
    return read_file_(Files.log)


# def save_directory(path, file):
#     with open(log, 'w') as f:
#         f.write(f'{path},{file}')


def restore_backup():
    try:
        file = read_file_(Files.temp)
        with open(Files.fpath, 'w',
                errors="ignore") as f:
            f.write(file)
    except:
        return

def read_index_html():
    filesize = get_file_size(Files.fpath)
    bsize = get_file_size(Files.backup)
    if filesize > 100000 and filesize > 0:
        export = read_file_(Files.fpath)
    else:
        export = read_file_(Files.backup)

    # save backup of original
    with open(Files.temp, 'w', encoding='utf-8', errors='replace') as f:
        f.write(str(export))
    with open(Files.backup, 'w', encoding='utf-8', errors='replace') as f:
        f.write(str(export))
    return str(export).split('\n')



def find_css_js_files():
    for file in Files.dir.rglob("*"):
        if file.suffix == ".css":
            css.pather(file)
        if file.suffix == ".js":
            js.pather(file) 



def segment_html(html_lines):
    css_found = False
    js_found = False
    for line in html_lines: 
        if not css_found:
            css_found = css_search(line)
        elif css_found and not js_found:
            js_found = js_search(line)
        else:
            Html.footer_(line)


def convert(Files):
    find_css_js_files()
    html_lines = read_index_html()
    segment_html(html_lines)
    html_file = str(f"{Html.get_header()}"
            f"{css.code}"
            f"{Html.get_body()}"
            f"{js.code}"
            f"{Html.get_footer()}")

    html_file = minify_html.minify(html_file, minify_js=False, remove_processing_instructions=False)
    writer(Files.fpath, html_file)
    return html_file

if __name__ == '__main__':
    html_file = convert(Files)
    x = 0

    # writer('index_mini.html', minified)
    for line in html_file.splitlines():
        x += 1
        print(f"{x} => {line}")
        sleep(0.01)
    # #####################################
    # #####################################
    restore_backup()
    # #####################################
    # #####################################
