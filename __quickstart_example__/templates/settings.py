from pathlib import Path
 

class Files:
	def __init__(self, workdir, directory, 
								filename, filepath 
								):
		self.workdir = workdir
		self.dir = directory
		self.fname = filename
		self.fpath = filepath
		self.temp = directory / f"temp_{filename}"
		self.backup = directory / f"backup_{filename}"
		self.log = directory / "log.txt"
 
#####################################



if __name__ == '__main__':
	pass