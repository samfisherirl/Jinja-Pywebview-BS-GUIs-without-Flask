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
from os.path import exists, join

css_paths = []
js_paths = []

lookfor_css = r"</head>"
lookfor_js = r"</body>"

# Use these literal markers as places for respective cod3e
# DO NOT include <script> <style> for insert markers, these will be added for
# marker locations. use outside of this is fine.

# assign directory
directory = str(getcwd())

filename = 'index.html'

# iterate over files in
# that directory


def find_css_js_files(directory, filename):
    for root, dirs, files in os.walk(directory):
        for filename in files:
            print(join(root, filename))
            if ".css" in filename:
                css_paths.append(join(root, filename))
            if ".js" in filename:
                js_paths.append(join(root, filename))


def read_file_return_contents(file):
    with open(file, 'r', errors='ignore') as f:
        return f.read()


def read_js():
    js = f"\n<script>\n"
    for file in js_paths:
        js = str(js + read_file_return_contents(file))
    return str(js + f"\n</script>\n" + lookfor_js)


def read_css():
    css = f"\n<style>\n"
    for file in css_paths:
        css = str(css + read_file_return_contents(file))
    return str(css + f"\n</style>\n" + lookfor_css)


def read_index_html(directory, filename):
    file = join(directory, f'backup_{filename}')
    if not exists(file):
        file = join(directory, filename)
    with open(file, 'r', errors="replace") as f:
        export = f.read()
        html_lines = export.split('\n')
    # save backup of original
    with open(join(directory, f'backup_{filename}'), 'w') as f:
        f.write(export)
    return html_lines


def access_directory():
    global directory_saved
    return directory_saved


def save_directory(path, file):
    global directory_saved, filename
    directory_saved = path
    filename = file


def restore_backup():
    global directory_saved, filename
    file = read_file_return_contents(
        str(directory_saved + f"\\backup_{filename}"))
    with open(str(directory_saved + f"\\{filename}"), 'w',
            errors="replace") as f:
        f.write(file)


def insert_js_css(html_lines):
    new_html = []
    for line in html_lines:
        if lookfor_css in line:
            new_html.append(read_css())  # insert css on marker
            continue
        elif lookfor_js in line:
            new_html.append(read_js())  # insert js on marker
            continue
        else:
            new_html.append(line)
    return new_html


def convert(directory, filename):
    directory = str(directory + "\\templates")
    save_directory(str(directory), filename)
    find_css_js_files(directory, filename)
    html_lines = read_index_html(directory, filename)
    new_html = insert_js_css(html_lines)
    with open(join(directory, filename), 'w', errors="replace") as f:
        f.write("\n".join(new_html))


if __name__ == '__main__':
    convert(directory, filename)
