from pathlib import Path
 

class Files:
	def __init__(self, workdir, directory, 
								filename, filepath, 
								tempname, temp, bup):
		self.workdir = workdir
		self.dir = directory
		self.fname = filename
		self.fpath = filepath
		self.tname = tempname
		self.temp = temp
		self.backup = bup
		self.log = directory / "log.txt"

#####################################

def file_settings():

		###################
		# working directory
		workdir = Path.cwd()
		###################
		if "templates" in str(workdir): 
			# if user specifies the templates directory
			directory = workdir
		else:
			directory = workdir / 'templates' 
		###################
		filename = "index.html"
		###################
		filepath = directory / filename
		###################
		tempname = f"temp_{filename}"
		backupname = f"backup_{filename}"
		###################
		temppath = directory / tempname
		backuppath = directory / backupname
		###################
		###################
		###################
		
#####################################
		return Files(workdir, 
				directory,
				filename, 
				filepath,
    		backupname,
				temppath,
    		backuppath)


if __name__ == '__main__':
		fil = file_settings()
		print(fil.dir)
