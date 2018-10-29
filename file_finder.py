import os, magic
from shutil import copyfile

pasting_dst = input('Enter path file to save files: ') # ../Logical Analysis
path = input('Enter path I should search: ') # ../../Logical
        
filetypes = {   'gif'     : os.path.join(pasting_dst, 'gifs/'),
                'jpeg'    : os.path.join(pasting_dst, 'jpegs/'),
                'html'    : os.path.join(pasting_dst, 'html/'),
                'zip'     : os.path.join(pasting_dst, 'zips/'),
                'png'     : os.path.join(pasting_dst, 'pngs/'),
                'pdf'     : os.path.join(pasting_dst, 'pdfs/'),
                'audio'   : os.path.join(pasting_dst, 'audio/'),
                'sqlite'  : os.path.join(pasting_dst, 'db/'),
                'tiff'    : os.path.join(pasting_dst, 'tiff/'),
                'ooxml'   : os.path.join(pasting_dst, 'ooxml/')}

def create_dirs():
    try:
        if not os.path.isdir(pasting_dst):
            os.makedirs(pasting_dst)
        if not os.path.isdir(path):
            os.makedirs(path)
        
        for filetype in filetypes:
            if not os.path.isdir(filetypes[filetype]):
                os.makedirs(filetypes[filetype])
    except Exception as e:
        print(f"Error: {e}")

def pathFinding():
    global pasting_dst, path, keyword
    for root, dirs, files in os.walk(path):
        for file in files:
            path_searched = os.path.join(root, file)
            print('\nPath: ' + path_searched)
            results = magic.from_file(path_searched)
            print(results)
            for filetype in filetypes:
                if filetype in results.lower():
                    copy_dst = filetypes[filetype] + file
                    copyfile(path_searched, copy_dst)
                    print('Saved to: ' + copy_dst)
                    os.remove(path_searched)

if __name__ == "__main__":
    create_dirs()
    pathFinding()
