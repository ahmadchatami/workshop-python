import shutil
shutil.copyfile('data.db', 'archive.db')
# 'archive.db' (Output)
shutil.move('/build/executables', 'installdir')
# 'installdir' (Output)