from pathlib import Path
from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
import webview
import templates.inject_js_css as inject_js_css
from os import walk, getcwd
import running_processes_and_paths as processes
import atexit

from os.path import join


#########################################
#########################################

from templates.settings import file_settings as file_settings

#########################################

# file_settings.py located in /templates/ folder

Files = file_settings()

#########################################
# Inject CSS and JS files into the HTML
inject_js_css.convert(Files)
######################################### 

###########running_processes############# 
data = processes.get()
######################################### 

# Create the environment
env = Environment(
    loader=FileSystemLoader(Files.dir),
    autoescape=select_autoescape()
)



# Get the template file
template = env.get_template(Files.fname)

# Create the list of words for the for loop
words = ["this is a for loop", "this is a jinja for loop", "for loop 3"]




# Render the HTML with the for loop and the CSS/JS files
view = template.render(
        data = data,
        words = words,
        subtitle = "To render the variables, insert the placeholder between {{}}"
        )

# Print the rendered HTML


# Exit handler to restore the original HTML file
def exit_handler():
    inject_js_css.restore_backup()

def start_window():
    windowTitle = "My window"
    webview.create_window(windowTitle, html=view, width=1100, height=900, fullscreen=False)
    webview.start()
    atexit.register(exit_handler)



def main():
    print(view)
    start_window()


# Execute the code
if __name__ == "__main__":
    main()