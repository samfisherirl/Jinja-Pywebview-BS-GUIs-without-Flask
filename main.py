from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
import webview
from templates import read_js_css

env = Environment(
                loader = FileSystemLoader('templates'),
                autoescape=select_autoescape()
)

#* Retrieving the template using the get_template() method
template = env.get_template("index.html")

class Data:
    word = "Dot Notation displayed"


words = ["this is a for loop", "this is a jinja for loop", "for loop 3", "for loop 4", "for loop 5", "for loop7"]
    
#* With the render() method I render the template 
#* Among the arguments of the render method I can pass data to be displayed in the 'templates' 
#* The data can be of any type variables, lists, dictionaries, objects, json
view = template.render(
        title = Data(),
        words = words,
        subtitle = "To render the variables, insert the placeholder between {{}}"
        )

print(view)


#* Extra: via the pywebview package I render the HTML I used 
#* in the example

if __name__ == "__main__":
    
    read_js_css.convert()

    windowTitle = "My window"
    webview.create_window(windowTitle, html = view)
    webview.start()
