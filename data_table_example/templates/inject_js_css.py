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
from os.path import exists, getsize
from time import sleep
from pathlib import Path 
try:
    from templates.settings import file_settings
except: 
    from settings import file_settings



Files = file_settings()

css_paths = []
js_paths = []

lookfor_css = r"</head>"
lookfor_js = r"</body>"

marker_start = """
<!-- marker...start...  -->
"""

marker_end =  """
<!-- marker...end... -->
"""

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


def read_file_(file):
    with open(file, 'r', errors='ignore') as f:
        return f.read()


def read_js(line):
    js = f"\n<script>\n"
    for file in js_paths:
        js = str(js + read_file_(file))
    return str(js + f"\n</script>\n" + lookfor_js)


def read_css(line):
    css = f"\n<style>\n"
    for file in css_paths:
        css = str(css + read_file_(file))
    return str(css + f"\n</style>\n" + lookfor_css)

def get_file_size(filename):
    try:
        return Path(filename).stat().st_size
    except:
        return 0

def clean_file(file_to_be_cleaned):
    x = 0
    clean_contents = []
    contents = read_file_(file_to_be_cleaned)
    for i in contents.split("\n"):
        if x == 1:
            if marker_end.strip() in i:
                x = 0
            else:
                continue
        elif marker_start.strip() in i:
            x = 1
            continue
        else:
            clean_contents.append(i) 
    return "\n".join(clean_contents)
            


# The code then checks if there are any files with a size greater than 100000 bytes, and if so it deletes them.
# If the terminal is closed without saving, the backup is not restored. To ensure doubling of injection, it 
# will clean the index file, as well  as leave markers on the index file as breadcrums

def read_index_html():
    filesize = get_file_size(Files.fpath)
    bsize = get_file_size(Files.backup)
    if filesize > 100000:
        export = read_file_(Files.backup)
    elif (filesize > 0) and (bsize < filesize) and (bsize > 10):
        export = read_file_(Files.backup)
    else: 
        export = read_file_(Files.fpath)
    # save backup of original
    with open(Files.temp, 'w') as f:
        f.write(export)
    with open(Files.backup, 'w') as f:
        f.write(export)
    return export.split('\n')


def access_directory():
    return read_file_(Files.log)


# def save_directory(path, file):
#     with open(log, 'w') as f:
#         f.write(f'{path},{file}')


def restore_backup():
    file = read_file_(Files.temp)
    with open(Files.fpath, 'w',
            errors="ignore") as f:
        f.write(file)


def segment_html(html_lines):
    css_found = False
    js_found = False
    html_header = []
    html_body = []
    html_footer = []
    _css_ = []
    _js_ = []
    new_html = []
    for line in html_lines:
        if css_found == False:
            if lookfor_css in line:
                _css_.append(read_css(line))  # insert css on marker
                css_found = True
                continue
            else:
                html_header.append(line)
                continue
        elif css_found == True and js_found == False:
            if lookfor_js in line:
                _js_.append(read_js(line))  # insert js on marker
                js_found = True
                continue
            else:
                html_body.append(line)
        else:
            html_footer.append(line)
    class Code:
        header = html_header
        css = _css_
        body = html_body
        js = _js_
        footer = html_footer
    return Code


def convert(Files):
    find_css_js_files()
    html_lines = read_index_html()
    Code = segment_html(html_lines)
    with open(Files.fpath, 'w', errors="replace") as f:
        f.write("\n".join(Code.header))
        f.write("\n".join(Code.css))
        f.write("\n".join(Code.body))
        f.write("\n".join(Code.js))
        f.write("\n".join(Code.footer))


if __name__ == '__main__':
    convert(Files)
    for i in range(8):
        print(f"{i}")
        sleep(1)
    restore_backup()
