
from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
import webview
import templates.inject_js_css as inject_js_css
from os import walk, getcwd

import atexit

from os.path import join


# "directory" needs to be the parent path 
# directly above the "templates" directory 
# ie where your main file is located

#########################################
directory = str(getcwd())
#########################################
filename = "index.html"
#########################################
# Inject CSS and JS files into the HTML
inject_js_css.convert(directory, filename)
#########################################


# Create the environment
env = Environment(
    loader=FileSystemLoader('templates'),
    autoescape=select_autoescape()
)



# Get the template file
template = env.get_template(filename)

# Create the list of words for the for loop
words = ["this is a for loop", "this is a jinja for loop", "for loop 3"]



class Data:
    title = "Dot notation title"
    subtext = "This is a dot notation subtext"

# Render the HTML with the for loop and the CSS/JS files
view = template.render(
        data = Data(),
        words = words,
        subtitle = "To render the variables, insert the placeholder between {{}}"
        )

# Print the rendered HTML
print(view)


# Exit handler to restore the original HTML file
def exit_handler():
    inject_js_css.restore_backup()


# Execute the code
if __name__ == "__main__":
    windowTitle = "My window"
    webview.create_window(windowTitle, html=view, width=1000, height=600, resizable=True, fullscreen=False)
    webview.start()
    atexit.register(exit_handler)
