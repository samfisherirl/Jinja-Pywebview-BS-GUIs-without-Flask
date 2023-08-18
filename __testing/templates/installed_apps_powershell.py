import subprocess
import collections

from pathlib import Path
cmd = r'reg query "HKCU\Software\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\Compatibility Assistant\Store" /s'

# appinfo_cmd1 = r'wmic datafile where Name="'
# appinfo_cmd2 = r'" list /format:list"'


def powershell(cmd):
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    return [line.decode().rstrip() for line in proc.stdout]

def clean_bytes(data):
    return [i.split("REG_BINARY")[0].strip() for i in data if "\\" in i]


class Paths:
    def __init__(self, path, name, id):
        self.path = path
        self.name = name
        self.id = id


def sort(paths):
    paths_keys = list(paths.keys())
    paths_keys.sort()
    return {i: paths[i] for i in paths_keys} # sorted dict

def classify(list_of_paths):
    paths = {}
    path = {}
    id = 0
    for p in list_of_paths:
        id += 1
        path = Path(f"{p}")
        paths[path.name] = Paths(path, path.name, id)
    return paths
    # alphabetically sort

def get():
    raw_pws_return = powershell(cmd)
    list_of_paths = clean_bytes(raw_pws_return)
    class_of_paths = classify(list_of_paths)
    return sort(class_of_paths)
    
if __name__ == '__main__':
    path_dic = get()
    for k, v in path_dic.items():
        print(f"{path_dic[k].name}")
    
    
'''
>>> from pathlib import Path
>>> p = Path("/home/user/Downloads/repo/test.txt")
>>> print(p.stem)
test
>>> print(p.name)
test.txt

def version_details(path):
return ["PowerShell.exe", f"[System.Diagnostics.FileVersionInfo]::GetVersionInfo(\"{path}\").FileVersion"]

'''