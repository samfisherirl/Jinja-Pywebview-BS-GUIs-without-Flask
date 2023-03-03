
class Tag:
    def __init__(self, open, close, lookfor_):
        self.open = open
        self.close = close
        self.lookfor_ = lookfor_
        
class Paths(Tag):
    def __init__(self, open, close, lookfor_):
        super().__init__(open, close, lookfor_)
        self.paths = []
        self.code = ""
        
    def pather(self, path):
        self.paths.append(path)

    def return_paths(self):
        string = ''
        return ["\n".join(i) for i in self.paths]

    def read_file_(self, file):
        with open(file, 'r', errors="replace") as f:
            return f.read()
            
    def construction(self):
        string = f"{self.open}"
        for file in self.paths:
            string = str(string + self.read_file_(file) + "\n")
        self.code = str(string + f"{self.close}" + self.lookfor_)

class Html:
    def __init__(self):
        self.header = []
        self.body = []
        self.footer = []

    def header_(self, line):
        self.header.append(line)

    def get_header(self):
        return str("\n".join(self.header))

    def body_(self, line):
        self.body.append(line)

    def get_body(self):
        return str("\n".join(self.body))

    def footer_(self, line):
        self.footer.append(line)

    def get_footer(self):
        return str("\n".join(self.footer))

    

if __name__ == '__main__':
    js = Paths('\n<script>\n', f"\n</script>\n")
    js.pather('nadjgklkjasdfgksdlf')
    js.construction(["1.txt", "1.txt"])
    print(js.open)
    print(js.open)
    print(js.return_paths)

