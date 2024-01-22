import os
from os.path import abspath, join, getsize

cutoff_amount = int(input("The amount of file you want to see:"))
file_size = int(input("How large of the files you want to see:"))

sizes = {}
count = 0
for top_dir, directories, files in os.walk('.'):
    for _file in files:
        full_path = abspath(join(top_dir,_file))
        size = getsize(full_path)
        if size > file_size:
            sizes[full_path] = size
            count += 1
sorted_results = sorted(sizes, key = lambda x:x[1])
print(f"{count} reults match you seach")

for i in sorted_results[:cutoff_amount]:
    print("path: {0} size: {1}".format(i, sizes[i]))


