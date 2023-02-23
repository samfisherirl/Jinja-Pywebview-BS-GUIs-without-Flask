# 
# Pywebview + Jinja2 + autoload CSS and JS (including Bootstrap) without restructuring standard website assets. 

 This will automatically iterate over files and folders in ./templates/, looking for *.js and *.css files, importing before loading. 


many changes upcoming, this is the first push and comes with many bugs but functions.  

simple jinja usage, pywebview template, with custom CSS and JS loader. 

loading js and css happens in this custom code: https://github.com/samfisherirl/Pywebview-and-Jinja2-with-CSS-and-JS-loader-template/blob/main/inject_js_css.py

Very simply, before the index file loads, main.py loops through all files in /templates/. For all files with  *.css, they get read and inserted right before the  `</header>` tag. Same thing for js happens before end of `</body>` tag. 
bootstrap, jquery all works, just place those files in the /template/ folder (anywhere, including "/templates/assets/bootstrap", keep your file structure as is) and that code will be injected before showing pywebview. Index backups are made to preserve original.

 ![image](https://user-images.githubusercontent.com/98753696/220928356-187783ac-c764-4c68-b735-6ed1a6fa9963.png)


![image](https://user-images.githubusercontent.com/98753696/220928471-4b52921c-de4b-4a93-b31f-727b00139f58.png)

![image](https://user-images.githubusercontent.com/98753696/220928704-8516e7a8-3e47-42e6-bac8-5d80f8eeb95f.png)

