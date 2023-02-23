from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
import webview
import templates.inject_js_css as inject_js_css
import templates.loop_files_folders as loop_files_folders
from os import walk, getcwd
from os.path import join
# "directory" needs to be the parent path 
# directly above the "templates" directory 
# ie where your main file is located


directory = str(getcwd())
filename = "index.html"
inject_js_css.convert(directory, filename)

env = Environment(
                loader = FileSystemLoader('templates'),
                autoescape=select_autoescape()
    )

#* Retrieving the template using the get_template() method
template = env.get_template("index.html")


data_obj_list = loop_files_folders.find_css_js_files(directory, filename)

words = ["this is a for loop", "this is a jinja for loop", "for loop 3", "for loop 4", "for loop 5", "for loop7"]
    
#* With the render() method I render the template 
#* Among the arguments of the render method I can pass data to be displayed in the 'templates' 
#* The data can be of any type variables, lists, dictionaries, objects, json
view = template.render(
        data = data_obj_list,
        words = words,
        subtitle = "To render the variables, insert the placeholder between {{}}"
        )

print(view)
 

#* Extra: via the pywebview package I render the HTML I used 
#* in the example

if __name__ == "__main__":
    
    windowTitle = "My window"
    webview.create_window(windowTitle, html = view, width = 1000, height = 600, resizable = True, fullscreen = False)
    webview.start()
