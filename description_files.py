import os

def generate_negative_description_file():
    with open('neg.txt', 'w') as f:
        for filename in os.listdir('negative'):
            f.write('negative/' + filename + '\n')

generate_negative_description_file()
#C:/Users/User/opencv/build/x64/vc15/bin/opencv_annotation.exe --annotations=pos.txt --images=positive/