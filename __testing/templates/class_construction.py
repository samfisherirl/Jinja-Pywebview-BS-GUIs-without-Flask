
class Tag:
    def __init__(self, open, close, lookfor_):
        self.open = open
        self.close = close
        self.lookfor_ = lookfor_
        
class JS_CSS(Tag):
    def __init__(self, open, close, lookfor_):
        super().__init__(open, close, lookfor_)
        self.paths = []
        self.code = ""
        
    def pather(self, path):
        self.paths.append(path)

    def return_paths(self):
        string = ''
        return ["\n".join(i) for i in self.paths]

    def _search(self, line):
        if self.lookfor_ in line:
            self.construction()
            return True
        else:
            return False

    @staticmethod
    def read_file_(file):
        with open(file, 'r', errors="replace") as f:
            return f.read()
            
    def construction(self):
        string = f"{self.open}"
        for file in self.paths:
            string = str(string + self.read_file_(file) + "\n")
        self.code = str(string + f"{self.close}" + self.lookfor_)

class Html:
    def __init__(self):
        self.code = []

    def add_line(self, line):
        self.code.append(line)

    def join_lines(self):
        self.code = str("\n".join(self.code))


    

if __name__ == '__main__':
    js = JS_CSS('\n<script>\n', "\n</script>\n", r"</body>")
    js.pather("index.html")
    js.pather("backup_index.html")
    js.construction()
    print(js.code)

