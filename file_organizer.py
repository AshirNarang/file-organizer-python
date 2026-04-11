"""
File Organizer Script

Organizes files into categories like Images, Videos, Documents, and Others.
Handles duplicate files and user input.

Author: Ashir Narang
"""

import os
import shutil

def move_file(src,dest_folder,filename):
    dest_path = os.path.join(dest_folder, filename)

    if os.path.exists(dest_path):
        name , ext = os.path.splitext(filename)
        i = 1
        
        while os.path.exists(dest_path):
            new_name = f"{name}_{i}{ext}"
            dest_path = os.path.join(dest_folder,new_name)
            i += 1
        
    shutil.move(src,dest_path)

def organize_files(folder_path):
    files = os.listdir(folder_path)

    images = ['.jpg', '.png', '.jpeg']
    videos = ['.mp4', '.mkv']
    docs = ['.pdf', '.txt', '.docx']

    image_folder = os.path.join(folder_path, "Images")
    video_folder = os.path.join(folder_path, "Videos")
    doc_folder = os.path.join(folder_path, "Documents")
    other_folder = os.path.join(folder_path, "Others")

    os.makedirs(image_folder, exist_ok=True)
    os.makedirs(video_folder, exist_ok=True)
    os.makedirs(doc_folder, exist_ok=True)
    os.makedirs(other_folder, exist_ok=True)

    image_moved = 0
    video_moved = 0
    documents_moved = 0
    others_moved = 0

    for file in files:
        file_path = os.path.join(folder_path, file)


        if os.path.isfile(file_path):
            ext = os.path.splitext(file)[1].lower()

            if ext in images:
                move_file(file_path, image_folder, file)
                image_moved += 1

            elif ext in videos:
                move_file(file_path, video_folder, file)
                video_moved += 1

            elif ext in docs:
                move_file(file_path, doc_folder, file)
                documents_moved += 1
            else:
                move_file(file_path, other_folder, file)
                others_moved += 1
    
    print(f"{image_moved} Images moved")
    print(f"{video_moved} Videos moved")
    print(f"{documents_moved} Documents moved")
    print(f"{others_moved} Other files moved")

def main():
    #folder_path = "C:/Users/ashir/OneDrive/Desktop/Ashir Python/Py Test Folder"
    folder_path = input("Enter Your Path:").replace("\\","/")

    if not os.path.exists(folder_path):
        print("invalid path")
        return
    
    print("Organizing files...")
    organize_files(folder_path)


if __name__ == "__main__":
    main()
