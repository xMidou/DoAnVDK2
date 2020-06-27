import pathlib


def rename_photos():
    path = pathlib.Path('.')/"dataset/3"
    count  = 0
    for folder in path.iterdir():
        folder.rename("./dataset/3/" + str(count) + ".jpg")
        count += 1
        print(count)

if __name__== "__main__":
     rename_photos()
    
