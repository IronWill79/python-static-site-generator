import os
import shutil

def main():
    source = './static'
    dest = './public'
    if os.path.exists(dest):
        shutil.rmtree(dest)
    shutil.copytree(source, dest)


if __name__ == "__main__":
    main()
