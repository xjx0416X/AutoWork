import os
from shutil import move


def files_distribution(folder_path):
    Doc=["txt", "pdf", "doc", "docx", "xls", "xlsx", "ppt", "pptx"]
    Img=["jpg", "jpeg", "png", "gif", "svg"]
    Music=["mp3", "wav", "aac", "flac", "m4a", "wma", "ape", "opus"]
    Video=["mp4", "avi", "flv", "wmv", "mov", "mkv", "webm"]
    installer=["exe", "msi", "pkg", "deb", "rpm", "dmg", "apk"]
    compressed=["zip", "tar", "gz", "bz2", "7z", "rar"]
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        file_extension = filename.split(".")[-1]
        if os.path.isfile(file_path):
            if file_extension in Doc:
                if not os.path.exists(os.path.join(folder_path, "Documents")):
                    os.makedirs(os.path.join(folder_path, "Documents"))
                move(file_path, os.path.join(folder_path, "Documents"))
            elif file_extension in Img:
                if not os.path.exists(os.path.join(folder_path, "Images")):
                    os.makedirs(os.path.join(folder_path, "Images"))
                move(file_path, os.path.join(folder_path, "Images"))
            elif file_extension in Music:
                if not os.path.exists(os.path.join(folder_path, "Music")):
                    os.makedirs(os.path.join(folder_path, "Music"))
                move(file_path, os.path.join(folder_path, "Music"))
            elif file_extension in Video:
                if not os.path.exists(os.path.join(folder_path, "Videos")): 
                    os.makedirs(os.path.join(folder_path, "Videos"))
                move(file_path, os.path.join(folder_path, "Videos"))
            elif file_extension in installer:
                if not os.path.exists(os.path.join(folder_path, "Installers")):
                    os.makedirs(os.path.join(folder_path, "Installers"))
                move(file_path, os.path.join(folder_path, "Installers"))
            elif file_extension in compressed:
                if not os.path.exists(os.path.join(folder_path, "Compressed")):
                    os.makedirs(os.path.join(folder_path, "Compressed"))
                move(file_path, os.path.join(folder_path, "Compressed"))
            else:
                if not os.path.exists(os.path.join(folder_path, "Others")):
                    os.makedirs(os.path.join(folder_path, "Others"))
                move(file_path, os.path.join(folder_path, "Others"))                                                                                                                                                                                                                            
        


def rename_files(folder_path,old_name,new_name):    
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            if old_name in filename:
                new_file_name = filename.replace(old_name, new_name)
                os.rename(file_path, os.path.join(folder_path, new_file_name))




def delete_empty_folders(folder_path):
    for root, dirs, files in os.walk(folder_path, topdown=False):
        for name in dirs:
            path = os.path.join(root, name)
            if not os.listdir(path):
                os.rmdir(path)



files_distribution("C:/Users/14523/Downloads")