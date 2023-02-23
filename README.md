# 
# This will automatically iterate over files and folders in ./templates/, looking for *.js and *.css files, importing before loading. 


many changes upcoming but first push. 

simple jinja usage, pywebview template, with CSS and JS loader. 

!Important!
Must use:     //{$insert_css$}
               //{$insert_js$}

as markers to position imports of css and js. This includes bootstrap, js, jquery, all autoloaded into pywebview

![image](https://user-images.githubusercontent.com/98753696/220867172-ea626610-6b0c-49c0-8fd6-6e24a2c94e56.png)

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



![image](https://user-images.githubusercontent.com/98753696/220868887-c0124c92-fbca-4646-ac30-b97b9106c3cd.png)
