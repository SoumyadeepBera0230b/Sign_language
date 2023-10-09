import os


for i in range(6, 25):
    path = f"./image/{chr(65+i)}"
    os.makedirs(path)
