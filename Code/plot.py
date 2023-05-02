import os
import re
import matplotlib.pyplot as plt

dir_path = 'Data/A'  # replace with the path to your directory
pattern = re.compile(r'.*\.(jpg|jpeg|png|gif)$', re.IGNORECASE)

folder_counts = {}
for root, dirs, files in os.walk(dir_path):
    folder_name = os.path.relpath(root, dir_path)
    folder_count = sum(1 for file in files if pattern.match(file))
    folder_counts[folder_name] = folder_count

x = list(range(len(folder_counts)))
y = list(folder_counts.values())

plt.bar(x, y)
plt.xticks(x, list(folder_counts.keys()), rotation=90)
plt.xlabel('Signs')
plt.ylabel('Number of image files')
plt.show()
