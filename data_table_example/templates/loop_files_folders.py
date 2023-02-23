
from os import walk, getcwd
from os.path import join


x = 0
directory = str(getcwd())
filename = "index.html"

class Data:
    def __init__(self, columnone, columntwo, columnthree, x):
        self.columnone = columnone
        self.columntwo = columntwo
        self.columnthree = columnthree
        self.index = x

data_obj_list = []

def find_css_js_files(directory, filename):
    global x
    for root, dirs, files in walk(directory):
        for filename in files:
            x = x + 1
            print(join(root, filename))
            path = root.split("\\")
            path = str(path[0] + "\\" + path[1] + "\\" + path[2] + "\\")
            data_obj_list.append(Data(path, filename, join(path, filename), x))
    return data_obj_list

if __name__ == "__main__":
    find_css_js_files(directory, filename)
    
    
    
    