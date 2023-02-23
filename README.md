# 
# This will automatically iterate over files and folders in ./templates/, looking for *.js and *.css files, importing before loading. 


many changes upcoming but first push. 

simple jinja usage, pywebview template, with CSS and JS loader. 

loading js and css happens in: https://github.com/samfisherirl/Pywebview-and-Jinja2-with-CSS-and-JS-loader-template/blob/main/templates/read_js_css.py

as markers to position imports of css and js. This includes bootstrap, js, jquery, all autoloaded into pywebview

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

 
