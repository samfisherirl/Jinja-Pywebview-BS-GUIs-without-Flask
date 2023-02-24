# 
# Pywebview + Jinja2 + autoload CSS and JS (including Bootstrap) without restructuring standard website assets. 

 This will automatically iterate over files and folders in ./templates/, looking for *.js and *.css files, importing before loading. 


many changes upcoming, this is the first push and comes with many bugs but functions.  

simple jinja usage, pywebview template, with custom CSS and JS loader. 

loading js and css happens in this custom code: https://github.com/samfisherirl/Pywebview-and-Jinja2-with-CSS-and-JS-loader-template/blob/main/inject_js_css.py

Very simply, before the index file loads, main.py loops through all files in /templates/. For all files with  *.css, they get read and inserted right before the  `</header>` tag. Same thing for js happens before end of `</body>` tag. 
bootstrap, jquery all works, just place those files in the /template/ folder (anywhere, including "/templates/assets/bootstrap", keep your file structure as is) and that code will be injected before showing pywebview. Index backups are made to preserve original.

![image](https://user-images.githubusercontent.com/98753696/221055533-0f7fc5b9-58af-41db-9af6-39a8a9712ffc.png)

See data table example for full code. In snippets, How the above data is created and displayed in python:


 ![image](https://user-images.githubusercontent.com/98753696/221068572-7578736a-683d-481f-acb8-ace63368d96c.png)





How I add render the view:
 
 ![image](https://user-images.githubusercontent.com/98753696/221068247-3405b219-f85d-43b1-b86a-b1d7c1b94c88.png)

      
      
      
                      
finally, I add the list to the index.html file:

![image](https://user-images.githubusercontent.com/98753696/221068165-a6798250-13d1-4e85-b1aa-1b5da9a06e6a.png)
