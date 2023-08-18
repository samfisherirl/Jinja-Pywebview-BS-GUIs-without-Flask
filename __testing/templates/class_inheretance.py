class Tag:
  def __init__(self, tag):
    self.tag = tag

class Paths(Tag):
  def __init__(self, tag, paths):
    super().__init__(tag)
    self.path1 = paths[0]
    self.path2 = paths[1]


js = Tag("this is a tag")
print(js.tag)

jp = Paths("this is a tag", ['C:\\', 'd:\\'])

print(jp.tag)
print(jp.path2)
