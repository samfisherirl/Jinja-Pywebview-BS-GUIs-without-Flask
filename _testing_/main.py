from pathlib import Path
from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
import webview
import templates.inject_js_css as inject_js_css
from templates import installed_apps_powershell
from templates import running_processes_and_paths
import atexit
import sys
from templates import handle_javascript

######################################### 
from templates.settings import file_settings as file_settings 

######################################### 
# file_settings.py located in /templates/ folder
Files = file_settings()

running_apps = running_processes_and_paths.get()
installed_apps = installed_apps_powershell.get()


def define_jinja2_view():
    inject_js_css.inject(Files)
    
    # corresponds to Data variable in HTML file
    env = Environment(
        loader=FileSystemLoader('templates'),
        autoescape=select_autoescape()
        )
    template = env.get_template(Files.fname)
    view = template.render(
        data=running_apps,
        installs=installed_apps,
        subtitle="To render the variables, insert the placeholder between {{}}"
        )
    return view


# Javascript functions
class API:
    def __init__(self):
        self.x = ''
        
    def launch_live_process(self, process):
        response = handle_javascript.return_object(process[0], Data)
        return response

    def error(self):
        raise Exception('This is a Python exception')


# Exit handler to restore the original HTML file
def exit_handler():
    inject_js_css.restore_backup()


def load_window():
    html_compiled = define_jinja2_view()
    api = API()
    windowTitle = "My window"
    webview.create_window(windowTitle, html=html_compiled, width=700, height=800, fullscreen=False, js_api=api)
    #inject_js_css.restore_backup()


def main():
    load_window()
    inject_js_css.restore_backup()
    # restore original index file before starting
    webview.start(debug=True)


# Execute the code
if __name__ == "__main__":
    main()
