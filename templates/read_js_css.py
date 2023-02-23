
import os
from os import getcwd
import os.path

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
	return str(js + "</script>" + lookfor_js)


def read_css():
	css = r"<style>"
	for i in css_paths:
		css = str(css + read_file_return_contents(i))
	return str(css + "</style>" + lookfor_css)



def read_html():
	if os.path.exists(os.path.join(directory, "templates", 'index_backup.html')):
		file = 'index_backup.html'
	else:
		file = 'index.html'

	with open(os.path.join(directory, "templates", file), 'r', errors="replace") as f:
		export = f.read()
		lines = export.split('\n')
	with open('index_backup.html', 'w') as f:
		f.write(export)	
	return lines


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


