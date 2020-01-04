#! /usr/bin/python3
'''
Walks through a folder tree and searches for files with a certain file extension (such as .pdf or .jpg). Copy these files from whatever location they are in to a new folder.
'''
import os, argparse, shutil


def selectiveCopy(folder, ext):
    print(f'given folder: {folder}')
    print(f'given ext: {ext}')

    destFolder = os.path.abspath('.')
    destFolder = os.path.join(destFolder, "output")
    print(f'dest folder: {destFolder}')
    try:
        os.makedirs(destFolder)
    except FileExistsError:
        print("'output' dir already exists!!!")

    print("about to walk")
    for folderName, subfolders, filenames in os.walk(folder):
        if os.path.samefile(folderName, destFolder):
            print(f'{folderName} is same as {destFolder}')
            continue
        for filename in filenames:
            if filename.endswith(ext):
                # print('FILE INSIDE ' + folderName + ': ' + filename)
                # print(f'Copying {filename} to {destFolder}')
                shutil.copy2(os.path.join(folderName, filename), destFolder)

    # print('')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("folder")
    parser.add_argument("extension")

    args = parser.parse_args()
    selectiveCopy(os.path.abspath(args.folder), args.extension)
