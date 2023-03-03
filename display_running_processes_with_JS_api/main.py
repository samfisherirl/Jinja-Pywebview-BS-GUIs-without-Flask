from pathlib import Path
from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
import webview
from templates import inject_js_css
from templates import running_processes_and_paths as processes
import atexit
import sys
from templates import handle_javascript

#########################################

from templates.settings import file_settings as file_settings

#########################################

# file_settings.py located in /templates/ folder

Files = file_settings()

#########################################
# Inject CSS and JS files into the HTML
inject_js_css.convert(Files)
######################################### 

# ##########_running_processes_###########

Data = processes.get()
######################################### 

# Create the environment
env = Environment(
    loader=FileSystemLoader('templates'),
    autoescape=select_autoescape()
)

# Get the template file
template = env.get_template(Files.fname)

# Render the HTML with the for loop and the CSS/JS files
view = template.render(
    data=Data,
    subtitle="To render the variables, insert the placeholder between {{}}"
    )


# Print the rendered HTML
class API:
    def __init__(self):
        self.x = ''

    def launch_live_process(self, process):
        response = processes.return_object(process[0], Data)
        return response

    def error(self):
        raise Exception('This is a Python exception')


# Exit handler to restore the original HTML file
def exit_handler():
    inject_js_css.restore_backup()


def start_window():
    api = API()
    windowTitle = "My window"
    webview.create_window(windowTitle, html=view, width=700, height=700, fullscreen=False, js_api=api)
    webview.start(debug=True)
    atexit.register(exit_handler)


def main():
    print(view)
    start_window()


# Execute the code
if __name__ == "__main__":
    main()
