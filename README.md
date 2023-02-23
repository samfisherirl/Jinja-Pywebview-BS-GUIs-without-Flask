# 
# Pywebview, Jinja2, autoload CSS and JS such as Bootstrap without restructuring standard website assets. 

 This will automatically iterate over files and folders in ./templates/, looking for *.js and *.css files, importing before loading. 


many changes upcoming, this is the first push and comes with many bugs but functions.  

simple jinja usage, pywebview template, with custom CSS and JS loader. 

loading js and css happens in this custom code: https://github.com/samfisherirl/Pywebview-and-Jinja2-with-CSS-and-JS-loader-template/blob/main/read_js_css.py

Very simply, before the index file loads, main.py loops through all files in /templates/. For all files with  *.css, they get read and inserted right before the  `</header>` tag. Same thing for js happens before end of `</body>` tag. 
This includes bootstrap, js, jquery, all autoloaded into pywebview.

![image](https://user-images.githubusercontent.com/98753696/220867172-ea626610-6b0c-49c0-8fd6-6e24a2c94e56.png)

        class Data:
            word = "Dot Notation displayed"


        words = ["this is a for loop", "this is a jinja for loop", "for loop 3", "for loop 4", "for loop 5", "for loop7"]

        view = template.render(
                title = Data(),
                words = words,
                subtitle = "To render the variables, insert the placeholder between {{}}"
                )

![image](https://user-images.githubusercontent.com/98753696/220905717-1330f53d-030f-4073-90fc-ed3cbe01c9ca.png)

 
