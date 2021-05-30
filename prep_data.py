import os
path = '/home/riki/Documents/Hakatons/mietDjango/rep/data/'
files = os.listdir(path)
file_name=''
print("input the name of the company u got letters from:")
input(file_name)
for index, file in enumerate(files):
    os.rename(os.path.join(path, file), os.path.join(path, ''.join([file_name ,str(index), '.pdf'])))