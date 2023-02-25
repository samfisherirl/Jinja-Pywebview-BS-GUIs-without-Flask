from pathlib import Path
 

class Files:
	def __init__(self, workdir, directory, 
								filename, filepath, 
								backupname, backuppath):
		self.workdir = workdir
		self.dir = directory
		self.fname = filename
		self.fpath = filepath
		self.bname = backupname
		self.bpath = backuppath
		self.log = directory / "log.txt"

#####################################

def file_settings():
		workdir = Path.cwd()
		directory = workdir / 'templates' 
		filename = "index.html"
		filepath = directory / filename
		backupname = f"backup_{filename}"
		backuppath = directory / backupname
		
#####################################
		return Files(workdir, 
				directory,
				filename, 
				filepath,
    		backupname,
				backuppath)


if __name__ == '__main__':
		fil = file_settings()
		print(fil.dir)
