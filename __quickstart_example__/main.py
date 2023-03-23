from pathlib import Path
from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
import webview
from templates import inject_js_css as inject_js_css 
import atexit
from templates.settings import Files
######################################### 

from templates.settings import file_settings

def file_settings():

		###################
		# working directory
		workdir = Path.cwd()
		###################
		if "templates" in str(workdir): 
			# if user specifies the templates directory
			directory = workdir
		else:
			directory = workdir / 'templates' 
		###################
		filename = "index.html"
		###################
		filepath = directory / filename
		###################
		
#####################################
		return Files(workdir, 
				directory,
				filename, 
				filepath)

Files = file_settings()

#########################################
# Inject CSS and JS files into the HTML

inject_js_css.convert(Files)

#########################################
# Inject CSS and JS files into the HTML
#########################################

items = ["apple", "bannana", "peach"]

class data:
    def __init__(self, item):
        self.item = item

def construct_objs():
    list_of_objs = []
    for i in items:
        list_of_objs.append(data(i))
    return list_of_objs


#########################################

data = construct_objs()

list = items

######################################### 

# Create the environment
env = Environment(
    loader=FileSystemLoader(Files.dir),
    autoescape=select_autoescape()
)

#########################################

# Get the template file
template = env.get_template(Files.fname)

#########################################


view = template.render(
        data = data,
        list = list,
        title = "To render the variables, insert the placeholder between {{}}"
        ) 


class Api:
    def __init__(self):
        self.cancel_heavy_stuff_flag = False

    def init(self):
        response = {
            'message': 'Hello from Python {0}'.format(sys.version)
        }
        return response


    def launch_live_process(self, name):
        response = {
            'message': 'Hello {0}!'.format(name)
        }
        print(response)
        return response

    def error(self):
        raise Exception('This is a Python exception')



# Exit handler to restore the original HTML file

def exit_handler():
    inject_js_css.restore_backup()
    

def start_window():
    api=Api()
    windowTitle = "My window"
    webview.create_window(windowTitle, html=view, width=500, height=600, fullscreen=False, js_api=api)
    webview.start()
    atexit.register(exit_handler)


def main():
    print(view)
    start_window()


# Execute the code
if __name__ == "__main__":
    main()