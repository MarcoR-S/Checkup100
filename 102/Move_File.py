import os
import shutil

from_dir = "C:/Users/maria/Downloads"
to_dir = "C:/Users/maria/OneDrive/Área de Trabalho/Arquivos_Documentos/"

list_of_files = os.listdir("from_dir")
print(list_of_files)

for file in list_of_files:
    #print(file)
    name, extension = os.path.splitext(file)
    print(name)
    if extension == '':
        continue

    if extension in ['.gif', '.png', '.jpg', '.jfif']:
        path1 = from_dir + '/'+ file
        path2 = to_dir + '/imageFile' 
        path3 = to_dir + '/imageFile/' + file

        if os.path.exists(path2):
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            shutil.move(path1, path3)
        