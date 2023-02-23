
# This script is used to combine all css and js files in the directory 
# and its subdirectories into a single file (index.html)
# It will also place all css and js at the bottom of the page, 
# which is useful for loading pages.  
# 
# It will also create a backup of the original index.html file, 
# and replace the original with the new one.  
# 
# 
# 
# This script is used in conjunction with the flask framework.  
# It is designed to be run from the command line in the directory 
# where the index.html file is located.  
# 
# 
# 
# The script will look for and use the following markers in the index.html file:
# 
# <HEAD> </HEAD>  - for css insertion
# <BODY> </B
import threading
import os
from os import getcwd
from os.path import exists, join

css_paths = []
js_paths = []


lookfor_css = r"</head>"
lookfor_js = r"</body>"

# Use these literal markers as places for respective cod3e
# DO NOT include <script> <style> for insert markers, these will be added for 
# marker locations. use outside of this is fine. 


# assign directory
directory = str(getcwd())



# iterate over files in
# that directory
for root, dirs, files in os.walk(directory):
	for filename in files:
		print(os.path.join(root, filename))
		if ".css" in filename:
			css_paths.append(os.path.join(root, filename))
		if ".js" in filename:
			js_paths.append(os.path.join(root, filename))

def read_file_return_contents(i):
	with open(i, 'r', errors='ignore') as f:
		return f.read()



def read_js():
	js = r"<script>"
	for i in js_paths:
		js = str(js + read_file_return_contents(i))
	return str(js + "</script>\n" + lookfor_js)


def read_css():
	css = r"<style>"
	for i in css_paths:
		css = str(css + read_file_return_contents(i))
	return str(css + "</style>\n" + lookfor_css)



def read_html():
		file = join(directory, "templates", 'index_backup.html')
		
		if exists(file):
			file = join(directory, "templates", 'index_backup.html')
		else:
			file = join(directory, "templates", 'index.html')

		with open(file, 'r', errors="replace") as f:
			export = f.read()
			lines = export.split('\n')
		with open(join(directory, "templates", 'index_backup.html'), 'w') as f:
			f.write(export)	
		return lines


threads = []
returns = []

def treds(lines):
	for line in lines:
		pass


  
def inserter(lines):
	new_html = []
	for line in lines:
		if lookfor_css in line:
			new_html.append(read_css()) # insert css on marker
			continue
		elif lookfor_js in line:
			new_html.append(read_js()) # insert js on marker
			continue
		else:
			new_html.append(line)
	
	return new_html



def convert():
	lines = read_html()
	new_html = inserter(lines)
	with open('index.html', 'w', errors="replace") as f:
		f.write("".join(new_html))

if __name__ == '__main__':
	convert()


