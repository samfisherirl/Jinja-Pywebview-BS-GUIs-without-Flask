# 
# Pywebview + Jinja2 + autoload CSS and JS (including Bootstrap) without restructuring standard website assets. 

 This will automatically iterate over files and folders in ./templates/, looking for *.js and *.css files, importing before loading. 


many changes upcoming, this is the first push and comes with many bugs but functions.  

simple jinja usage, pywebview template, with custom CSS and JS loader. 

loading js and css happens in this custom code: https://github.com/samfisherirl/Pywebview-and-Jinja2-with-CSS-and-JS-loader-template/blob/main/read_js_css.py

Very simply, before the index file loads, main.py loops through all files in /templates/. For all files with  *.css, they get read and inserted right before the  `</header>` tag. Same thing for js happens before end of `</body>` tag. 
This includes bootstrap, js, jquery, all autoloaded into pywebview.

 ![image](https://user-images.githubusercontent.com/98753696/220928356-187783ac-c764-4c68-b735-6ed1a6fa9963.png)


 ![image](https://user-images.githubusercontent.com/98753696/220921720-296a935a-f479-4761-b50c-f1b96ebe65fd.png)



![image](https://user-images.githubusercontent.com/98753696/220921326-9da8f698-16cf-4a4e-92ee-3fa03fcc1906.png)

