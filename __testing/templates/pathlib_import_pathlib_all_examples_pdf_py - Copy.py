from pathlib import Path
'''
###########
# graphic pdf 
https://github.com/samfisherirl/pathlib-quickstart-guide/blob/master/Pathlib_Cheat_Sheet.pdf
###########
'''
#Get the home directory 
home_dir = Path.home()

# Get the path to the current working directory 
cwd = Path.cwd()

# Get the path to the current Python file (does not work in 
# Jupyter Notebooks)
curr_file = Path(__file__)

# Get the first parent folder path 
one_above = Path.cwd().parent

# Get the Nth parent folder path 
mul_above = Path.cwd().parents[0]
# Join paths 
joined_path = cwd / 'Output' / 'FolderName'

#  Create a directory if it does not exist
# exist_ok: to ignore 'FileExistsError' if the target directory already 
# exists
your_path = "c:\\"
your_path.mkdir(exist_ok=True)

example_file = "file.txt"

# Check if the path is a folder (returns True/False) 
your_path.is_dir()

# Check if the path is a file (returns True/False) 
your_path.is_file()

# Get the file name (returns string) 
file_name = example_file.name

# Get the file name w/o extension (returns string)
file_name = example_file.stem

# Get the file extension (returns string) 
file_extension = example_file.suffix

# Iterate over files in a directory
target_dir = cwd / "Sample Files"
for file in your_path.iterdir():
  print(file)
  
# Iterate over files in a directory combined with suffix:
target_dir = cwd / "Sample Files"
for file in target_dir.iterdir():
  if file.suffix == ".xlsx":
    print(file)
    
# Iterate over files in a directory incl. sub folder(s)
target_dir = cwd / "Sample Files"
for file in target_dir.rglob("*"):
  print(file)
