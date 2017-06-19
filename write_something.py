
import os

for dirpath, dirnames, filenames in os.walk(os.curdir):
    for file1 in filenames:
        if file1.endswith(".py"):
		print dirpath+"/"+file1
		with open(dirpath+"/"+file1, 'r') as f:
			lines = f.readlines()
		with open(dirpath+"/"+file1, 'w') as f:
			for i,line in enumerate(lines):
				if i == 0:
					f.write('##########\n')
				f.write(line)
			f.close()
            #os.remove(os.path.join(dirpath, file1))
		
    
