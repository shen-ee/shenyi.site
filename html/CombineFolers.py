import shutil
import os
from PIL import Image
paths = ['/home/th/Desktop/VisionLab/Data_2/val/left/',
'/home/th/Desktop/VisionLab/Data_2/val/right/',
'/home/th/Desktop/VisionLab/Data_2/train/left/',
'/home/th/Desktop/VisionLab/Data_2/train/right/']
target_path = '/home/th/Desktop/VisionLab/Data_2/combined/'
for folder in os.listdir(target_path):
	target_folder = target_path + folder + '/'
	for path in paths:
		sub_path = path+folder+'/'
    		print("processing"+sub_path)
    		for im in os.listdir(sub_path):
        		if os.path.splitext(im)[1]=='.jpg':
                		im_dir = sub_path+im
                		img = Image.open(im_dir)
                		img.save(target_folder + im)
			else:
				print('unknown file')


shutil.copyfile("hello.py", "hello2.py")    #hello.txt内容复制给hello2.txt
shutil.move("hello.py", "../")              #hello.txt复制到当前目录的父目录，然后删除hello.txt
shutil.move("hell2.txt", "hello3.txt")      #hello2.txt移到当前目录并命名为hello3.py, 然后删除