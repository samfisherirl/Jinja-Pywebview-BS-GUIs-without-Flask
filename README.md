# 
# Pywebview + Jinja2 + autoload CSS and JS (including Bootstrap) without restructuring standard website assets. 

 This will automatically iterate over files and folders in ./templates/, looking for *.js and *.css files, importing before loading. 


many changes upcoming, this is the first push and comes with many bugs but functions.  

simple jinja usage, pywebview template, with custom CSS and JS loader. 

loading js and css happens in this custom code: https://github.com/samfisherirl/Pywebview-and-Jinja2-with-CSS-and-JS-loader-template/blob/main/inject_js_css.py

Very simply, before the index file loads, main.py loops through all files in /templates/. For all files with  *.css, they get read and inserted right before the  `</header>` tag. Same thing for js happens before end of `</body>` tag. 
bootstrap, jquery all works, just place those files in the /template/ folder (anywhere, including "/templates/assets/bootstrap", keep your file structure as is) and that code will be injected before showing pywebview. Index backups are made to preserve original.

 ![image](https://user-images.githubusercontent.com/98753696/221052925-8b98d7c1-89ba-49d7-8dc7-925d247937cc.png)

See data table example for full code. First, How the above data is created and displayed in python:


    class Data:
        def __init__(self, columnone, columntwo, columnthree, x):
            self.columnone = columnone
            self.columntwo = columntwo
            self.columnthree = columnthree
            self.index = x

    data_obj_list = []
    x = 0

    def find_css_js_files(directory, filename):
        global x
        for root, dirs, files in walk(directory):
            for filename in files:
                x = x + 1
                data_obj_list.append(Data(path, filename, join(path, filename), x))


How I add the list to the view:

      view = template.render(
              data = data_obj_list,
              )
             
      webview.create_window(windowTitle, html = view
      
      
      
                      
finally, I add the list to the index.html file:
       <tbody>

           {% for item in data %}
       <tr>
           <td>{{ item.index }}</td>
           <td>{{ item.columnone }}</td>
           <td>{{ item.columntwo }}</td>
           <td>{{ item.columnthree }}</td>
       </tr>
           {% endfor %}
