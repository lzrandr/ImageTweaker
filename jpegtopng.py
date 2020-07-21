import sys
import os
from PIL import Image



in_folder = sys.argv[1]
out_folder = sys.argv[2]

if not os.path.exists(out_folder):	
	os.makedirs(out_folder)
for img_file in os.listdir(in_folder):

	opened_img = Image.open(f'{in_folder}{img_file}')
		
	opened_img.save(out_folder+os.path.splitext(img_file)[0]+'.png','png')
	print(out_folder+os.path.splitext(img_file)[0]+'.png')	
