import os
os.chdir('C:\\Users\\USER\\Documents\\Internship on AI\\Image classification using CNN\\simple_images\\harrypotter\\')
i = 1
for file in os.listdir():
    src = file
    dst = str(i)+".jpg"
    os.rename(src, dst)
    i += 1
