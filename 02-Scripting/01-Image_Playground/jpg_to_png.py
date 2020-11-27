import sys
import os
from PIL import Image

# grab first and second arguments passed on terminal
actual_folder = sys.argv[1]
new_folder = sys.argv[2]

# check is new folder exists, if not create
if not os.path.exists(new_folder):
    os.makedirs(new_folder)

# loop through Pokedex, grap each image, convert and save to new folder
for filename in os.listdir(actual_folder):
    img = Image.open(f'{actual_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    # print(clean_name)
    img.save(f'{new_folder}{clean_name}.png', 'png')
    print('all done!')
