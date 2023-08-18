import subprocess
import re


def check_for_description(input_text):
    # matches paths within powershell output
    #
    try:
        if "Description" in str(input_text.split(":")[0]).strip():
            return True
        else:
            return None
    except:
        return None


x = 0


class Apps:
    def __init__(self, title, path, exe, id):
        self.title = title
        self.path = path
        self.exe = exe
        self.id = id



def construct_app_obj(desc, path):
    # matches paths within powershell output
    #
    global x
    app = {}
    line = path.split(':')
    try:
        x = x + 1
        path = str(f'{line[1]}:{line[2]}')
        exe = path.split("\\")
        exe = (exe[(len(exe)) - 1])
        title = str(desc.split(':')[1].strip()).strip("\r\n")
        if title != "":
            app = Apps(
                title.replace("\\r\\n", ""),
                path.strip(),
                exe.strip(),
                int(x)
                )
        # dic = {
        #       'title': str(desc.split(':')[1].strip()),
        #       'path': str(f'{line[1]}:{line[2]}')
        #       }
    except:
        pass
    return app


def powershell():
    cmd = 'powershell "gps | where {$_.MainWindowTitle } | select Description,Id,Path | Format-List'
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    return [line.decode("utf-8", errors="replace") for line in proc.stdout]
    

def loop_output(output_text):
    x = 0
    apps = {}
    app_dic = {}
    for powershell_line in output_text:
        if check_for_description(powershell_line):
            app_dic = construct_app_obj(
                output_text[x],
                str(f'{output_text[x + 2]}'))
            if app_dic != {}:
                apps[int(x)] = app_dic
            x += 1
        else:
            x += 1
    return apps


""" Here is the explanation for the code above:
1. The function get() returns the list of all installed applications
2. The function powershell() runs the powershell command and returns the output as a list
3. The function loop_output() loops through the output and returns a list of all installed applications """



def get():
    output_text = powershell()
    # [print(output_text) for output_text in output_text]
    apps = loop_output(output_text)
    return apps


if __name__ == '__main__':
    cls = get()
    for i in cls.keys():
        print(cls[i].title)


