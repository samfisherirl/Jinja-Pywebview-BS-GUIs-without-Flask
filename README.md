
# Inject CSS and JS (including Bootstrap) into  Pywebview + Jinja2 without flask or restructuring standard website assets. 

This solution takes Pywebview with Jinja2, and loops through all files in your ./assets/ or ./templates/ looking for any file with *.js and *.css extensions. Read, and inject the code into (eg.) index.html prior to Pywebview displaying in Webview. 
# 



This is a new projects as of 2/23/23, expect small bugs and changes daily. 

#




Very simply, before the index file loads, main.py loops through all files in /templates/. For all files with  *.css, they get read and inserted right before the  `</header>` tag, inbetween `<style>`and `</style>`. Same thing for js happens before end of `</body>` tag. 
bootstrap, jquery all works, just place those files in the /template/ folder (anywhere, including "/templates/assets/bootstrap", keep your file structure as is) and that code will be injected before showing pywebview. Index backups are made to preserve original.

![image](https://user-images.githubusercontent.com/98753696/221055533-0f7fc5b9-58af-41db-9af6-39a8a9712ffc.png)

See <a href="https://github.com/samfisherirl/Pywebview-and-Jinja2-with-CSS-and-JS-loader-template/tree/main/data_table_example">data table example for full code</a>.  


![image](https://user-images.githubusercontent.com/98753696/221068165-a6798250-13d1-4e85-b1aa-1b5da9a06e6a.png)
](https://i.imgur.com/ii9M91d.gif)
