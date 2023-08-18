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

import minify_html

from time import sleep
from pathlib import Path

try:
    from templates.settings import file_settings
    from templates.class_construction import JS_CSS, Html
except:
    from settings import file_settings
    from class_construction import JS_CSS, Html

Files = file_settings() 

Html_header = Html()
Html_body = Html()
Html_footer = Html()


# Use these literal markers as places for respective cod3e
# DO NOT include <script> <style> for insert markers, these will be added for
# marker locations. use outside of this is fine.

# assign directory 

filename = 'index.html'

log = Files.log

js = JS_CSS('\n<script>\n', "\n</script>\n", r"</body>")
css = JS_CSS('\n<style>\n', "\n</style>\n", r"</head>")


            
def writer(name, content):
    with open(name, 'w', encoding='utf-8', errors="replace") as f:
        f.write(content)


# iterate over files in
# that directory


def read_file_(file):
    with open(file, 'r', errors='replace', encoding='utf-8') as f:
        return str(f.read())




def css_search(line):
        if css.lookfor_ in line:
            css.construction()

def js_search(line):
        if js.lookfor_ in line:
            js.construction()
            return True
        else:
            Html_body.add_line(line)
            return False



def get_file_size(filename):
    try:
        return JS_CSS(filename).stat().st_size
    except:
        return 0

def demo_print_code(html_file):
    x = 0
    print("\n\n\n=> printing code line by line")
    for i in range(5):
        y = 5 - int(i)
        print(f"=>{y}")
        sleep(1)
    for line in html_file.splitlines():
        x += 1
        print(f"{x} => {line}")
        sleep(0.1)
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
    
    try:
        bsize = get_file_size(Files.backup)
        filesize = get_file_size(Files.fpath)
    except:
        filesize = get_file_size(Files.fpath)
    try:
        if filesize < 100000 and filesize > 0:
            export = read_file_(Files.fpath)
        else:
            export = read_file_(Files.backup)
    except:
        export = read_file_(Files.fpath)
    # save backup of original
    writer(Files.temp, export)
    writer(Files.backup, export)
    return str(export).split('\n')



def find_css_js_files():
    for file in Files.dir.rglob("*"):
        if file.suffix == ".css":
            css.pather(file)
        if file.suffix == ".js":
            js.pather(file) 



def insert_html(html_lines):
    css_found = False
    js_found = False
    for line in html_lines: 
        if not css_found:
            css_found = css._search(line)
            if not css_found:
                Html_header.add_line(line)
        elif css_found and not js_found:
            js_found = js._search(line)
            if not js_found:
                Html_body.add_line(line)
        else:
            Html_footer.add_line(line)
    Html_header.join_lines()
    Html_body.join_lines()
    Html_footer.join_lines()


def inject(Files):
    find_css_js_files()
    html_lines = read_index_html()
    insert_html(html_lines)
    html_file = str(f"{Html_header.code}"
            f"{css.code}"
            f"{Html_body.code}"
            f"{js.code}"
            f"{Html_footer.code}")

    html_file = minify_(html_file)
    writer(Files.fpath, html_file)
    return html_file


if __name__ == '__main__':
    html_file = inject(Files)
    demo_print_code(html_file)
    restore_backup()