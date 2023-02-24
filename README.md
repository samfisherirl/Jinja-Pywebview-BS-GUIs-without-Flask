
# Inject CSS and JS (including Bootstrap) into  Pywebview + Jinja2 without flask or restructuring standard website assets. 

This solution takes Pywebview with Jinja2, and loops through all files in your ./assets/ or ./templates/ looking for any file with *.js and *.css extensions. Read, and inject the code into (eg.) index.html prior to Pywebview displaying in Webview. 
# 



This is a new projects as of 2/23/23, expect small bugs and changes daily. 

#




Very simply, before the index file loads, main.py loops through all files in /templates/. For all files with  *.css, they get read and inserted right before the  `</header>` tag, inbetween `<style>`and `</style>`. Same thing for js happens before end of `</body>` tag. 
bootstrap, jquery all works, just place those files in the /template/ folder (anywhere, including "/templates/assets/bootstrap", keep your file structure as is) and that code will be injected before showing pywebview. Index backups are made to preserve original.


 https://i.imgur.com/Cj5Dif9.gif


